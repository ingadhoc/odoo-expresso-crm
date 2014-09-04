# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
{   'active': True,
    'author': 'Sistemas Adhoc',
    'category': 'None',
    'demo_xml': [],
    'depends': ['expresso_crm','base_import'],
    'description': 'Expresso CRM Module.',
    'init_xml': [],
    'installable': True,
    'name': 'Expresso CRM Modifications',
    'test': [],
    'update_xml': ['view/partner_view.xml', 
                'view/campaign_detail_view.xml',
                'security/security.xml',
		# 'report/campaign_detail_report_view.xml',
                'data/expresso_crm.course.csv', 
                'security/ir.model.access.csv'],
    'demo': [
                'data/demo/res.company.csv',
                'data/demo/expresso_crm.educational_plan.csv',
                'data/demo/expresso_crm.campaign.csv',
                'data/demo/res.partner.csv',
                'data/demo/expresso_crm.campaign_detail.csv',
                'data/demo/res.users.csv',
            ],
    'version': '0.1',
    'website': 'http://www.sistemasadhoc.com.ar/'}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
