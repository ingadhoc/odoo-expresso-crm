from openerp.osv import fields,osv
from openerp import tools

class report_campaign_detail(osv.osv):
    _name = "campaign_detail.report"
    _description = "Campaign Details Report"
    _auto = False
    _columns = {
        'campaign_id_x': fields.many2one('expresso_crm.campaign', 'Campaign', readonly=True, relate=True),
        'partner_id_x':fields.many2one('res.partner', 'School', readonly=True),
        'course_id_x':fields.many2one('expresso_crm.course', 'Course', readonly=True),
        'educational_plan_id_x':fields.many2one('expresso_crm.educational_plan', 'Educational Plan', readonly=True),
        'potential_value_x': fields.integer('Potential', readonly=True),
        'real_value_x': fields.integer('Real', readonly=True)
        }

    _order = 'id, campaign_id desc, partner_id, course_id, educational_plan_id'

    def init(self, cr):
    # def init(cr):
        cr.execute("""
        CREATE OR REPLACE VIEW report_campaign_detail AS (
        SELECT
            T1.id as id
            T1.campaign_id as campaign_id,
            T1.partner_id as partner_id,
            T1.course_id as course_id,
            T1.educational_plan_id as educational_plan_id,
            T1.valor_pot as potential_value,
            T2.valor_real as real_value
        FROM
            vw_tabla1 T1 FULL JOIN vw_tabla2 T2 ON T2.course_id = T1.course_id
        ORDER BY
            campaign_id
     )""")

report_campaign_detail()