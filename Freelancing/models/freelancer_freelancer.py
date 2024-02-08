#-*- coding: utf-8 -*-

from odoo import models, fields

class Freelancer(models.Model):
    _name = 'freelancer.freelancer'
    _description = 'Freelancer Information'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')]
    )
    email = fields.Char(string='Email', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    address = fields.Text(string='Address')
    hourly_rate = fields.Float(string='Hourly Rate', default=0)
    skills = fields.Text(string='Skills')
