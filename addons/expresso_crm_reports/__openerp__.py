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


{
    'active': True,
    'name': 'Expresso CRM Reports',
    'category': 'Customer Relationship Management', 
    'version': '1.0',
    'description': """
    This module provides Expresso CRM with informative reports
    """,
    'author': 'Sistemas Adhoc',
    'website': 'http://www.sistemasadhoc.com.ar/',
    'depends': ['expresso_crm','base_import','board'],
    'update_xml': [
                    'report/expresso_crm_report_view.xml',
                    'board_crm_view.xml',
                    'security/ir.model.access.csv',
                    'security/security.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
