# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class AccountInvoice(models.Model):
    _inherit = ['account.invoice', 'automatic.mail.mixin']
    _name = 'account.invoice'

    @api.multi
    def invoice_validate(self):
        res = super(AccountInvoice, self).invoice_validate()
        # send confirmation mail only for Customer invoices
        out_invoice = self.filtered(
                lambda r: r.type == 'out_invoice')
        out_invoice.force_confirm_mail_send()
        return res
