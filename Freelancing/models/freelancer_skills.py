#-*- coding: utf-8 -*-

from odoo import fields, models

class FreelancerSkills(models.Model):
    _name = 'freelancer.skills'
    _description = 'Freelancer Skills'
    _sql_constraints = [
        ('unique_type_name', 'UNIQUE(s_name)', 'Property type name must be unique!')
    ]
    _order = 's_name'

    s_name = fields.Char(string='Skill Name', required=True)
    freelancer_ids = fields.Many2many('freelancer.freelancer', string='Freelancer')
    