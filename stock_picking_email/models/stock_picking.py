# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class StockPicking(models.Model):
    _inherit = ['stock.picking', 'automatic.mail.mixin']
    _name = 'stock.picking'

    def should_send_mail(self):
        res = super(StockPicking, self).should_send_mail()
        # send confirmation mail only for Customer delivery
        selected_pik = res.filtered(
            lambda p: p.picking_type_id.code == 'outgoing')
        if selected_pik:
            return selected_pik
        else:
            return False

    @api.multi
    def write(self, vals):
        res = super(StockPicking, self).write(vals)
        if vals.get('date_done', False):
            selected_pik = self.should_send_mail()
            if selected_pik:
                selected_pik.force_confirm_mail_send()
        return res
