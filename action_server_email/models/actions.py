# -*- coding: utf-8 -*-
# © 2013-TODAY Akretion (http://www.akretion.com)
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import time

from openerp import api, fields, models

class ActionsServer(models.Model):
    _inherit = "ir.actions.server"

    email_template_id = fields.Many2one('mail.template', 'Email Template')
        
    @api.model
    def _get_states(self):
        type_selection = super(ActionsServer, self)._get_states()
        option = ('mail_template', 'Email Template')
        if option not in type_selection:
            type_selection.append(option)        
        return type_selection

    @api.multi
    def run(self):
        super(ActionsServer, self).run()
        user = self.user
        for action in self:
            cxt = self._get_eval_context(action)
            expr = eval(str(action.condition), cxt)
            if not expr:
                continue
            if action.state == 'mail_template':
                template_obj = self.env['mail.template']
                email_template = action.email_template_id
                obj_id = ctx[obj] and ctx[obj].id or False
                email_template.send_mail(ctx[obj].id, force_send=False)
        return False




