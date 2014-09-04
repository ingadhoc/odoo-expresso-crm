# -*- coding: utf-8 -*-
from openerp import api, models, fields


class partner(models.Model):

    """"""

    _inherit = 'res.partner'

    @api.one
    @api.depends('course_ids')
    def _get_courses(self):
        self.courses = len(self.course_ids)

    @api.one
    @api.depends('course_ids', 'course_average_classrooms')
    def _get_classrooms_total(self):
        self.classrooms_total = len(self.course_ids) * self.course_average_classrooms

    courses = fields.Integer(
        compute="_get_courses",
        string='Number of courses',
        readonly=True,
        store=True,)
    classrooms_total = fields.Integer(
        compute="_get_classrooms_total",
        string='Classrooms total',
        readonly=True,
        store=True)
    is_school = fields.Boolean(
        string='Is School?',
        change_default=True)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
