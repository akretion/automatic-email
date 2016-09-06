# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models

class EmailTemplate(models.Model):
    _inherit = 'mail.template'

    action_server_ids = fields.One2many(
    	'ir.actions.server', 'email_template_id', string='Action Server')

