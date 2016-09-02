# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale Email',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': 
    """
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        "action_server_email",
        "sale"
    ], 
    'data': [ 
        'data/sale_data.xml',
    ],
    'installable': True,
}
