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

class campaign_detail(osv.osv):
    """"""
    
    _name = 'expresso_crm.campaign_detail'
    _description = 'campaign_detail'

    _columns = {
        'company_id': fields.many2one('res.company', string='Company'),
        'course_ids': fields.many2many('expresso_crm.course', 'expresso_crm_campaign_detail_ids_course_ids_rel', 'campaign_detail_id', 'course_id', string='Courses', required=True), 
        'partner_id': fields.many2one('res.partner', string='School', context={'default_is_company':True,'default_is_school':True}, domain=[('is_school','=','True')], ondelete='cascade', required=True), 
        'educational_plan_id': fields.many2one('expresso_crm.educational_plan', string='Educational Plan', required=True), 
        'campaign_id': fields.many2one('expresso_crm.campaign', string='Campaign', required=True), 
    }

    _defaults = {
        'company_id': lambda s,cr,uid,c: s.pool.get('res.company')._company_default_get(cr, uid, 'sgr.document', context=c),
    }

    _order = "campaign_id desc, partner_id, educational_plan_id"

    _constraints = [
    ]




campaign_detail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
