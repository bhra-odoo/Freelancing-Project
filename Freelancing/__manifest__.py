#-*- coding: utf-8 -*-
#Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Freelancing',
    'description': '',
    "category": "Industry/Freelancing",
    'summary': 'Freelancing project',
    'installable': True,
    'application': True,
    'depends': ['base'],
    'license': 'OEEL-1',
    'version': '1.0',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/freelancer_report_templets.xml',
        'report/freelancer_report.xml',
        'views/freelancer_bids_view.xml',
        'views/freelancer_tasks_views.xml',
        'views/freelancer_skills_views.xml',
        'views/freelancer_project_views.xml',
        'views/freelancer_client_views.xml',
        'views/freelancer_freelancer_views.xml',
        'views/freelancer_menu.xml',
    ]
}
