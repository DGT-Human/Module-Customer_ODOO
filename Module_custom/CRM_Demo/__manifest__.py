# -*- coding: utf-8 -*-
{
    'name': "Demo_CRM",

    'summary': """
        Hello wolrd""",

    'description': """
        Hello wolrd
    """,

    'author': "DGT",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'data': [
        'views/person_views.xml',
    ],
    # any module necessary for this one to work correctly
    'depends': ['base'],

}
