#-*- coding: utf-8 -*-

from odoo import fields, models

class ProjectReport(models.Model):
    _name = 'freelancer.project.report'
    _description = 'Project Report'

    name = fields.Char(string='Report Name', required=True)
    project_id = fields.Many2one('freelancer.project', string='Project', required=True)
    date = fields.Date(string='Report Date', required=True)
    description = fields.Text(string='Description')
