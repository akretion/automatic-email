# -*- coding: utf-8 -*-
###############################################################################
#
#   action_server_email for OpenERP
#   Copyright (C) 2013-TODAY Akretion <http://www.akretion.com>.
#   @author Florian DA COSTA <florian.dacosta@akretion.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp.osv import fields, osv
import time


class actions_server(osv.osv):
    _inherit = "ir.actions.server"

    _columns = {
        'email_template_id': fields.many2one('email.template', 'Email Template'),
    }

    def __init__(self, pool, cr):
        super(actions_server, self).__init__(pool, cr)
        option = ('email_template', 'Email Template')
        type_selection = self._columns['state'].selection
        if option not in type_selection:
            type_selection.append(option)

    def run(self, cr, uid, ids, context=None):
        super(actions_server, self).run(cr, uid, ids, context=context)
        user = self.pool.get('res.users').browse(cr, uid, uid)
        for action in self.browse(cr, uid, ids, context):
            obj = None
            obj_pool = self.pool.get(action.model_id.model)
            if context.get('active_model') == action.model_id.model and context.get('active_id'):
                obj = obj_pool.browse(cr, uid, context['active_id'], context=context)
            cxt = {
                'self': obj_pool,
                'object': obj,
                'obj': obj,
                'pool': self.pool,
                'time': time,
                'cr': cr,
                'context': dict(context), # copy context to prevent side-effects of eval
                'uid': uid,
                'user': user
            }
            expr = eval(str(action.condition), cxt)
            if not expr:
                continue
            if action.state == 'email_template':
                template_obj = self.pool.get('email.template')
                template_id = action.email_template_id.id
                template_obj.send_mail(cr, uid, template_id, obj.id, force_send=False, context=context)
        return False




