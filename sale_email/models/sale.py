# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import time

from openerp import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
      

    @api.multi
    def action_quotation_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        ## ---> Set BreakPoint
        import pdb;
        pdb.set_trace()
        self.ensure_one()
        action_dict = super(SaleOrder, self).action_quotation_send()
        if self.env.context.get('send_email'):
            ctx = action_dict['context']
            template_id = False
            ir_model_data = self.env['ir.model.data']
            try:
                template_id = self.env.ref(
                    'sale_email.email_template_sale_confirmation')
            except ValueError:
                template_id = False
            if template_id:
                ctx.update({
                'default_use_template': bool(template_id.id),
                'default_template_id': template_id.id,
                })
                action_dict.update({'context': ctx})
        return action_dict




