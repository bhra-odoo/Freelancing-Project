#-*- coding: utf-8 -*-

from odoo import fields, models

class Task(models.Model):
    _name = 'freelancer.task'
    _description = 'Project Task'

    name = fields.Char(string='Task Name', required=True)
    client_id = fields.Char(related="project_id.client_id.name", string='Client', required=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('freelancer.project', string='Project', required=True)
    deadline = fields.Date(string='Deadline', required=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To', required=True)
    tag_ids = fields.Many2many('freelancer.tags',string='Tags')
    completed = fields.Boolean(string='Completed')
