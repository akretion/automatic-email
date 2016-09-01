# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Action Server Email',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': 
    """
    Add new type in action_server in order to send an email from a workflow action.
    Can be linked with an email template.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        "mail",
    ], 
    'init_xml': [],
    'update_xml': [ 
        'views/actions_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
}
