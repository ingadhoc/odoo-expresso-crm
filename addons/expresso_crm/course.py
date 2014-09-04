# -*- coding: utf-8 -*-
##############################################################################
#
#    Expresso CRM
#    Copyright (C) 2014 Grupo ADHOC
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class course(osv.osv):
    """"""
    
    _name = 'expresso_crm.course'
    _description = 'course'

    _columns = {
        'name': fields.char(string='Name', required=True),
        'campaign_detail_ids': fields.many2many('expresso_crm.campaign_detail', 'expresso_crm_campaign_detail_ids_course_ids_rel', 'course_id', 'campaign_detail_id', string='campaign_detail_ids'), 
        'partner_id': fields.many2many('res.partner', 'expresso_crm___course_ids_rel', 'course_id', 'partner_id', string='&lt;no label&gt;'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




course()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
