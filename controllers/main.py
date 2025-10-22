# Importamos el módulo http de Odoo para declarar controladores (rutas HTTP).
from odoo import http
# Importamos "request" para acceder a la petición HTTP (método, datos, etc.).
from odoo.http import request

# Definimos una clase que agrupa rutas web relacionadas con la calculadora.
class WebCalcController(http.Controller):

    # Definimos una ruta accesible en /calculator.
    # - type="http": ruta clásica (no es JSON RPC).
    # - auth="public": cualquiera puede acceder (sin iniciar sesión).
    # - website=True: usa el motor de plantillas del Website de Odoo.
    # - methods=["GET","POST"]: acepta formulario (POST) y también mostrar la página (GET).
    # - csrf=True: protección contra ataques CSRF (debe enviarse el token en el form).
    @http.route(
        "/calculator",
        type="http",
        auth="public",
        website=True,
        methods=["GET", "POST"],
        csrf=True,
    )
    def calculator(self, **post):
        # Lee los parámetros enviados por formulario (si es POST).
        # Si es GET, probablemente vengan como None.
        a = post.get("a")
        b = post.get("b")
        op = post.get("op", "add")  # si no viene "op", por defecto "add" (sumar).

        # Variables para enviar a la plantilla: resultado numérico o mensaje de error.
        result = None
        error = None

        # Función interna para convertir cadenas a float de forma segura.
        def to_float(x):
            try:
                return float(x)  # intenta convertir, si falla lanza excepción
            except Exception:
                return 0.0       # si falla la conversión, usa 0.0 como valor seguro

        # Si el método HTTP fue POST, significa que enviaron el formulario.
        if request.httprequest.method == "POST":
            # Convertimos A y B a números (float).
            fa = to_float(a)
            fb = to_float(b)

            # Según la operación seleccionada, calculamos.
            if op == "add":
                result = fa + fb
            elif op == "sub":
                result = fa - fb
            elif op == "mul":
                result = fa * fb
            elif op == "div":
                # Dividir entre cero no está permitido → ponemos error.
                if fb == 0:
                    error = "No se puede dividir entre cero"
                else:
                    result = fa / fb
            else:
                # Si alguien manda una operación rara, devolvemos error.
                error = "Operación no válida"

        # Preparamos el diccionario de valores que la plantilla (HTML) va a usar.
        values = {
            "a": a or "",              # si a es None, enviamos "" para no romper el input
            "b": b or "",
            "op": op,                  # operación actual para marcarla seleccionada en el <select>
            "result": result,          # número o None
            "error": error,            # texto o None
        }
        # Renderizamos la plantilla QWeb "clocky_electronic"
        # y le pasamos "values" para pintar la página.
        return request.render("clocky_electronic", values)
