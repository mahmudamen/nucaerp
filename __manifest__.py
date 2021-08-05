# -*- coding: utf-8 -*-
{
    'name': "nucaerp",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
       new urban communities authority
    """,

    'author': "Nuca",
    'website': "http://www.newcities.gov.eg/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'erp',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/nucaerp.xml',
        'views/menu.xml',
        'wizards/testwizard.xml',
        'views/Contract.xml',
        'views/Parties.xml',
        'views/Socialstatus.xml',
        'views/Functionalclass.xml',
        'views/wheel.xml',
        'views/Followup.xml',
        'views/Job.xml',
        'views/Savelocation.xml',
        'views/Typecontact.xml',
        'views/Lectures.xml',
        'views/PersonalData.xml',
        'views/ContractsData.xml',
        'views/Weapon.xml',
        'views/Archive.xml',
        'views/Wireless.xml',
        'views/shelfs.xml',
        'Report/report.xml',
        'Report/report_template.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
    'installable': True,
    'auto_install': False,
}
