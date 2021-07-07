# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Backlink Generator',
    'version': '1.1',
    'summary': 'Backlink Generator',
    'sequence': 15,
    'description': 'Backlink Generator',
    'category': 'New',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/backlink_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/backlink_view.xml',
        'views/backlink_item_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
