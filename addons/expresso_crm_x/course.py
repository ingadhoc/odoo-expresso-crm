# -*- coding: utf-8 -*-
##############################################################################
#
#    Expresso CRM
#    Copyright (C) 2013 Grupo ADHOC
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
from openerp import SUPERUSER_ID

class course(osv.osv):
    """"""
    
    _name = 'expresso_crm.course'
    _inherit = [ 'expresso_crm.course' ]    

    _columns = {
    }

    _defaults = {
    }

    def create(self, cr, uid, vals, context=None):
        id = super(course, self).create(cr, uid, vals, context=context)
        ir_values_obj = self.pool.get('ir.values')
        all_courses_ids = self.search(cr, uid, [], context=context)        
        ir_values_obj.set_default(cr, SUPERUSER_ID, 'res.partner', "course_ids", all_courses_ids, condition='is_school=true', for_all_users=True)
        return id

#Intenando hacer que se actualice la lista al borrar uno
    # def unlink(self, cr, uid, ids, context=None):
    #     #id = super(course, self).unlink(cr, uid, ids, context=context)
    #     return super(course, self).unlink(cr, uid, ids, context=context)
    #     ir_values_obj = self.pool.get('ir.values')
    #     all_courses_ids = self.search(cr, uid, [], context=context)        
    #     ir_values_obj.set_default(cr, SUPERUSER_ID, 'res.partner', "course_ids", all_courses_ids, condition='is_school=true', for_all_users=True)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
