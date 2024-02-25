#-*- coding: utf-8 -*-

from odoo import fields, models

class Project(models.Model):
    _name = 'freelancer.tags'
    _description = 'Freelance Tags'
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'Property type name must be unique!')
    ]
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')
