# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale order Email',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description':
    """
        Send an automatic email when an sale order is validated.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        "base_automatic_mail",
        "sale"
    ],
    'data': [
        'views/sale_view.xml',
    ],
    'installable': True,
}
