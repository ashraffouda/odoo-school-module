# -*- coding: utf-8 -*-
{
    'name': "School",

    'summary': """School Module """,

    'description': """
       School module used to manage students and courses
    """,

    'author': "Ashraf Fouda",
    'website': "http://www.ashraf-fouda.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
#         'security/security.xml',
        'templates.xml',
        'views/school.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
