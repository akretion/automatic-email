# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AutomaticMail(models.AbstractModel):
    _name = 'automatic.mail.mixin'

    automail_confirm_sent = fields.Boolean(
        default=False, copy=False,
        help="It indicates that the confirmation mail has been sent.")

    @api.multi
    def _get_mail_auto_template(self):
        '''
        Get the mail template
        '''
        model_id = self.env['ir.model'].search([('model', '=', self._name)])
        template_obj = self.env['mail.template']
        template_id = template_obj.search(
            [('model_id', '=', model_id.id), ('automail_confirm', '=', True)],
            limit=1)
        return template_id

    @api.multi
    def force_confirm_mail_send(self):
        template_id = self._get_mail_auto_template()
        if template_id:
            for obj in self:
                template_id.send_mail(obj.id)
                obj.automail_confirm_sent = True
        return True

    def should_send_mail(self):
        # Send confirmation message only once
        selected_obj = self.filtered(
            lambda r: r.automail_confirm_sent == False)
        return selected_obj or self.browse(False)

class MailComposeMessage(models.Model):
    _inherit = 'mail.compose.message'

    @api.multi
    def send_mail(self, auto_commit=False):
        context = self._context
        if context.get('auto_confirm_mail') and \
            context.get('default_model') and context.get('default_res_id') and\
                context.get('mark_confirm_sent'):
            model_name = context.get('default_model')
            obj = self.env[model_name].browse(context['default_res_id'])
            obj = obj.with_context(mail_post_autofollow=True)
            obj.automail_confirm_sent = True
        return super(MailComposeMessage, self).send_mail(
            auto_commit=auto_commit)
