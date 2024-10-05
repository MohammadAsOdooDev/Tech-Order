# -*- coding: utf-8 -*-
{
    'name': "tech_order",

    'summary': "Meal Orders Module",

    'description': """
Long description of module's purpose
    """,

    'author': "Mohammad Hamdan",
    'website': "https://www.MohammadAsDev.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/meal.xml',
        'views/tag.xml',
        'views/category.xml',
        'views/order.xml',
        'views/templates.xml',
        'views/item.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

