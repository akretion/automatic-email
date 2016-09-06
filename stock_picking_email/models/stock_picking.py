# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class StockPicking(models.Model):
    _inherit = ['stock.picking', 'automatic.mail.mixin']
    _name = 'stock.picking'

    @api.multi
    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if vals.get('date_done', False):
            # send confirmation mail only for Customer delivery
            outgoings = self.filtered(
                lambda p: p.picking_type_id.code == 'outgoing')
            outgoings.force_confirm_mail_send()
        return res
