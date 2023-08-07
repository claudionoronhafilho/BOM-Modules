# -*- coding: utf-8 -*-
{
    'name': 'BOM Product Cost Price',
    'version': '16.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'Calculate Total BOM Cost Price of Product and Show BOM Cost in BOM Form and Product Form, BOM Product Cost Price, BOM Cost Price, Update Product Cost from BOM.',
    'description': """
        This module allow to calculate total bill of material cost of product and show bom cost in bom form view, 
        product template and product variant form view.
        Cost calculate based on bom product line and quantity.
        Calculate BoM cost price of Manufacturing Product or BoM product.
        Users can see BoM Product Cost on Product Template.
        Users can see BoM Product Cost on Product Variant.
    """,
    'sequence': 1,
    'author': 'Futurelens',
    'website': 'http://thefuturelens.com',
    'depends': ['mrp', 'product'],
    'data': [
        'views/mrp_bom_views.xml',
        'views/product_template_view.xml',
    ],
    'images': [
        'static/description/banner_bom_product_cost.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
    'price': 10,
    'currency': 'EUR',
}
