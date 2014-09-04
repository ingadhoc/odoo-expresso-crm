# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License AS
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

from openerp.osv import fields,osv
from openerp import tools

class expresso_crm_report(osv.osv):

    _name = "expresso.crm.report"
    _description = "Campaign Details Report"
    _auto = False

    _columns = {
        'campaign_id': fields.many2one('expresso_crm.campaign', 'Campaign', readonly=True),
        'partner_id':fields.many2one('res.partner', 'School', readonly=True),
        'course_id':fields.many2one('expresso_crm.course', 'Course', readonly=True),
        'educational_plan_id':fields.many2one('expresso_crm.educational_plan', 'Educational Plan', readonly=True),
        'company_id': fields.many2one('res.company', 'Company', readonly=True),
        'type': fields.char('Type', readonly=True),
        'course_average_classrooms': fields.integer('Classrooms', readonly=True),
        'value': fields.integer('Value', readonly=True)
    }

    _order = 'campaign_id desc, company_id, partner_id, course_id, educational_plan_id, value, id'

    def init(self, cr):

        tools.drop_view_if_exists(cr, 'expresso_crm_report')
        cr.execute("""
            CREATE OR REPLACE VIEW expresso_crm_report AS  (-- La primera parte refiere a los registros potenciales, se obtiene de combinar todos los potenciales colegios, planes educativos, cursos y se le agrega
-- un campo que toma el nombre de Potential, y un valor que es siempre igual a 1 
-- La primera fila consiste en la creacion del ID que debe ser unico por fila, se realiza un concatenado, y se agrega una P al final para diferenciar de los reales

SELECT
                    CAST(campaign.id AS text) || CAST(partner_courses.partner_id AS text) || CAST(course_id AS text) || CAST(plan.id AS text) || 'P' AS id,
                    campaign.id AS campaign_id,
                    partner_courses.partner_id AS partner_id,
                    partner_courses.course_id AS course_id,
                  partner_courses.company_id AS company_id,
                  
                    plan.id AS educational_plan_id,
            'Potential' as type,
            partner_courses.course_average_classrooms,  
                    1 AS value
            
                FROM
                    expresso_crm_campaign campaign, 

                    (select expresso_crm___course_ids_rel.partner_id, expresso_crm___course_ids_rel.course_id, res_partner.company_id, res_partner.course_average_classrooms
                    from (expresso_crm___course_ids_rel full join res_partner on expresso_crm___course_ids_rel.partner_id = res_partner.id) where res_partner.is_school = true) partner_courses,
expresso_crm_educational_plan plan where partner_id IS NOT NULL 

UNION

-- La segunda parte refiere a los registros reales, se obtiene de la tabla campaign details, cargada por los usuarios y se le agrega
-- un campo que toma el nombre de Real, y un valor que es siempre igual a 1 
-- La primera fila consiste en la creacion del ID que debe ser unico por fila, se realiza un concatenado, y se agrega una R al final para diferenciar de los potenciales


SELECT 
                    CAST(campaign_id AS text) || CAST(partner_id AS text) || CAST(course_id AS text) || CAST(educational_plan_id AS text) || 'R'  AS id,
                    campaign_id,
                    partner_id,
                    course_id,
                    company_id,
                    educational_plan_id,
                    'Real' as type,
                    course_average_classrooms,  
                    1 AS value
                FROM 
                    (SELECT 
                        id AS course_id_pk
                    FROM 
                        expresso_crm_course) AS courses
                FULL JOIN
                    (SELECT
                        campaign.campaign_id,
                        campaign.partner_id,
                        campaign.course_id,
                        campaign.company_id,
                        campaign.educational_plan_id,
                        res_partner.course_average_classrooms
                    FROM 
                        (expresso_crm_campaign_detail 
                    FULL JOIN 
                        expresso_crm_campaign_detail_ids_course_ids_rel 
                    ON 
                        expresso_crm_campaign_detail.id = expresso_crm_campaign_detail_ids_course_ids_rel.campaign_detail_id) campaign, 

                        res_partner where res_partner.id = campaign.partner_id) AS details
                ON 
                    courses.course_id_pk = details.course_id
                WHERE campaign_id IS NOT NULL)
""")

expresso_crm_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
