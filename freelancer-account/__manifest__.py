#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'freelancer_account',
    'description': '',
    'summary': 'Freelancer Account',
    'installable': True,
    'application': True,
    'depends': ['Freelancing', 'account'], 
    'license': 'OEEL-1',
    'version': '1.0',
    'data' : [
        'security/ir.model.access.csv',
        'report/invoice_report.xml',
        'views/account_move_views.xml'
    ]
}
