#-*- coding: utf-8 -*-

from odoo import models, fields

class Freelancer(models.Model):
    _name = 'freelancer.freelancer'
    _description = 'Freelancer Information'

    name = fields.Char(string='Name', required=True)
    freelancer_image = fields.Image(string='Image', max_width=1920, max_height=1920)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')]
    )
    email = fields.Char(string='Email', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    address = fields.Text(string='Address')
    hourly_rate = fields.Float(string='Hourly Rate', default=0)
    skill_ids = fields.Many2many('freelancer.skills', string='Skills')
    project_id = fields.Many2one('freelancer.project')
