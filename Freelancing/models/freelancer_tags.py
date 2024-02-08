#-*- coding: utf-8 -*-

from odoo import fields, models

class Project(models.Model):
    _name = 'freelancer.tags'
    _description = 'Freelance Tags'

    name = fields.Char('Name', required=True, translate=True)
    color = fields.Integer(string='Color')
    project_ids = fields.Many2many('freelancer.project', string='Projects')
    task_ids = fields.Many2many('freelancer.task', string='Tasks')
