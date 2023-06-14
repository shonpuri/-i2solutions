# -*- coding: utf-8 -*-
{
    'name': "I2 Reports",
    'summary': "Reports",
    'description': "I2 Custom Report",
    'category': 'Sale',
    'version': '16.0.0',
    'author':'Dishicreation',
    'depends': ['sale'],
    'data': [
            # 'security/ir.model.access.csv',
            'reports/sale_order_info_template.xml',
            'reports/sale_order_invoice_template.xml',
            'reports/sale_order_waybill_template.xml',
            'reports/report.xml',
            # 'wizard/create_new_wizard.xml',
            'views/company.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}