#-*- coding: utf-8 -*-

from odoo import fields, models

class Project(models.Model):
    _name = 'freelancer.tags'
    _description = 'Freelance Tags'

    name = fields.Char(string='Name', required=True)
