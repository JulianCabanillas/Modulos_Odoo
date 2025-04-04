# -*- coding: utf-8 -*-
{
    'name': "Zoo",

    'summary': "Zoo",

    'description': """
Zoo
    """,

    'author': "ZeroHaker",
    'website': "https://www.Zoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/animal_view.xml',
        'views/cuidador_view.xml',
        'views/espacio_view.xml',
        'views/menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

