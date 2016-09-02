# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import time

from openerp import api, fields, models

class AccountInvoice(models.Model):
    _inherit = "account.invoice"
      
    @api.multi
    def action_invoice_sent(self):
        '''
        If the mail is sent automaticlly we use invoice confirmtion template
        '''
        action_dict = super(AccountInvoice, self).action_invoice_sent()
        if self.env.context.get('send_email'):
            ctx = action_dict['context']
            template_id = False
            try:
                template_id = self.env.ref(
                    'sale_email.email_template_invoice_confirmation')
            except ValueError:
                template_id = False
            if template_id:
                ctx.update({
                'default_use_template': bool(template_id.id),
                'default_template_id': template_id.id,
                })
                action_dict.update({'context': ctx})
        return action_dict


    @api.multi
    def force_invoice_send(self):
        for invoice in self:
            email_act = invoice.action_invoice_sent()
            if email_act and email_act.get('context'):
                email_ctx = email_act['context']
                email_ctx.update(default_email_from=invoice.company_id.email)
                invoice.with_context(email_ctx).message_post_with_template(email_ctx.get('default_template_id'))
        return True

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice,self).invoice_validate()
        self.with_context(send_email=True).force_invoice_send()
        return res

