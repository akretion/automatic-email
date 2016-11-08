# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
import base64


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    invoice_mail_sent = fields.Boolean('Invoice Mail Sent')

    @api.multi
    def _should_send_invoice_mail(self):
        self.ensure_one()
        if self.invoice_status == 'invoiced' and not self.invoice_mail_sent:
            return True
        else:
            return False

    @api.multi
    def send_invoice_mail(self, invoices):
        self.ensure_one()
        attach_obj = self.env['ir.attachment']
        template = self.env.ref('sale_invoice_email.sale_invoice_mail_tmpl')
        mail_vals = template.generate_email(self.id)
        mail = self.env['mail.mail'].create(mail_vals)
        i = 1
        attachment_ids = []
        for invoice in invoices:
            result, format = self.pool['report'].get_pdf(
                self._cr, self._uid, [invoice.id], 'account.report_invoice',
                context=self._context), '.pdf'
            result = base64.b64encode(result)
            filename = self.name
            if i > 1:
                filename = filename + '_' + str(i)
            filename = filename + format
            i += 1
            attachment_data = {
                'name': filename,
                'datas_fname': filename,
                'datas': result,
                'res_model': 'mail.message',
                'res_id': mail.mail_message_id.id,
            }
            attachment_ids.append(attach_obj.create(attachment_data).id)
        mail.write({'attachment_ids': [(6, 0, attachment_ids)]})
        self.write({'invoice_mail_sent': True})

    @api.multi
    def action_done(self):
        super(SaleOrder, self).action_done()
        for sale in self:
            invoices = self.invoice_ids.filtered(
                lambda i: i.state not in ('draft', 'cancel'))
            if sale._should_send_invoice_mail() and invoices:
                sale.send_invoice_mail(invoices)
