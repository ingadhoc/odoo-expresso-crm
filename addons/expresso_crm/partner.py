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

class partner(osv.osv):
    """"""
    
    _name = 'res.partner'
    _inherits = {  }
    _inherit = [ 'res.partner' ]

    def _get_courses(self, cr, uid, ids, name, args, context=None):
        """"""
        raise NotImplementedError

    def _get_classrooms_total(self, cr, uid, ids, name, args, context=None):
        """"""
        raise NotImplementedError

    _columns = {
        'courses': fields.function(_get_courses, type='integer', arg=None, fnct_inv_arg=None, obj=None, string='Number of courses', readonly=True),
        'course_average_classrooms': fields.integer(string='Average classrooms per course'),
        'classrooms_total': fields.function(_get_classrooms_total, type='integer', arg=None, fnct_inv_arg=None, obj=None, string='Classrooms total', readonly=True),
        'is_school': fields.boolean(string='Is School?'),
        'calendar': fields.selection([(u'north', u'North'), (u'south', u'South')], string='Calendar'),
        'campaign_detail_ids': fields.one2many('expresso_crm.campaign_detail', 'partner_id', string='Campaign Details'), 
        'course_ids': fields.many2many('expresso_crm.course', 'expresso_crm___course_ids_rel', 'partner_id', 'course_id', string='Courses'), 
    }

    _defaults = {
        'course_average_classrooms': 1,
    }


    _constraints = [
    ]




partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
