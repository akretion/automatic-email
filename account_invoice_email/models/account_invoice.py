# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class AccountInvoice(models.Model):
    _inherit = ['account.invoice', 'automatic.mail.mixin']
    _name = 'account.invoice'

    def should_send_mail(self):
        res = super(AccountInvoice, self).should_send_mail()
        # send confirmation mail only for Customer invoices
        selected_inv = res.filtered(
            lambda r: r.type == 'out_invoice')
        if selected_inv:
            return selected_inv
        else:
            return False

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice, self).invoice_validate()
        selected_inv = self.should_send_mail()
        if selected_inv:
            selected_inv.force_confirm_mail_send()
        return res
