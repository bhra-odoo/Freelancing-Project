#-*- coding: utf-8 -*-

from odoo import fields, models

class FreelancerSkills(models.Model):
    _name = 'freelancer.skills'
    _description = 'Freelancer Skills'

    s_name = fields.Char(string='Skill Name', required=True)
    freelancer_ids = fields.Many2many('freelancer.freelancer', string='Freelancer')
    