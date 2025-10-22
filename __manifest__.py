{
    "name": "Website Calculator (Account Dep)",
    "summary": "Calculadora simple en el Website con lógica Python (depende de Facturación)",
    "version": "17.0.1.0.0",
    "author": "Clocky App",
    "license": "LGPL-3",
    "category": "Website",
    "depends": ["website", "account"],
    "data": [
        "views/templates.xml",
        "data/website_menu.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "fact_electronic_clocky/static/src/scss/styles.scss",
        ],
    },
    "installable": True,
    "application": False,
}
