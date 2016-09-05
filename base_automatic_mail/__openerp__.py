# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Automatic Email confirmation',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description':
    """
    Generic module used to send confirmation by automatic email
    of any object (sale, invoice, ...).
    This module must be inherited to define wich action is used to send
    email.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        "mail",
    ],
    'init_xml': [],
    'update_xml': [
        'views/mail_template_view.xml',
    ],
    'installable': True,
}
