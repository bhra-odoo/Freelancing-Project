#-*- coding: utf-8 -*-

from odoo import models, fields

class Freelancer(models.Model):
    _name = 'freelancer.freelancer'
    _description = 'Freelancer Information'

    name = fields.Char(string='Username', required=True)
    user_id = fields.Many2one('res.users', string='Name')
    image_1920 = fields.Binary(related='user_id.image_1920', string='Image')
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
