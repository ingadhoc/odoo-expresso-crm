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


{   'active': False,
    'author': u'Grupo ADHOC',
    'category': 'base.module_category_hidden',
    'demo_xml': [],
    'depends': [u'base'],
    'description': u'Expresso CRM. Schools database management',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Expresso CRM',
    'test': [],
    'update_xml': [   u'security/expresso_crm_group.xml',
                      u'view/partner_view.xml',
                      u'view/course_view.xml',
                      u'view/campaign_detail_view.xml',
                      u'view/campaign_view.xml',
                      u'view/educational_plan_view.xml',
                      u'view/expresso_crm_menuitem.xml',
                      u'data/partner_properties.xml',
                      u'data/course_properties.xml',
                      u'data/campaign_detail_properties.xml',
                      u'data/campaign_properties.xml',
                      u'data/educational_plan_properties.xml',
                      u'data/partner_track.xml',
                      u'data/course_track.xml',
                      u'data/campaign_detail_track.xml',
                      u'data/campaign_track.xml',
                      u'data/educational_plan_track.xml',
                      'security/ir.model.access.csv'],
    'version': u'7.0.1.1',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
