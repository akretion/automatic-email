# -*- coding: utf-8 -*-
###############################################################################
#
#   action_server_email for OpenERP
#   Copyright (C) 2013-TODAY Akretion <http://www.akretion.com>.
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


{
    'name': 'Stock Invoice Email',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': 
    """
        Send an automatic email when an invoice is created in order to confirm an expedition.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': [
        "action_server_email",
        "stock"
    ], 
    'data': [ 
        'invoice_data.xml',
        'invoice_workflow.xml',
    ],
    'demo': [],
    'installable': True,
}
