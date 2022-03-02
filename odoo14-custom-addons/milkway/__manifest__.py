# -*- coding: utf-8 -*-
{
    'name': "milkway",

    'summary': """
        Instalacion de un nuevo módulo Odoo, Personalizar campos y funciones de nuestro módulo e
        incluir entradas de menu,widgets. Introducir datos en nuestra aplicación , para posteriormente hacer consultas postgresql""",

    'description': """
        Simulacro Examen
    """,

    'author': "Enrique García-Palacios Blasco",
    'website': "https://github.com/Enriquegpb/odoodevs",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application':True, 
    'category': 'Marketing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}