#-*- coding: utf-8 -*-

from odoo import fields, models

class Project(models.Model):
    _name = 'freelancer.project'
    _description = 'Freelance Project'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    client_id = fields.Many2one('freelancer.client', string='Client', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    tasks = fields.One2many('freelancer.task', 'project_id', string='Tasks', required=True)
    tags = fields.Many2many('freelancer.tags', string='Tags')
