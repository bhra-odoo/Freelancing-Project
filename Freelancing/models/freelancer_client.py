#-*- coding: utf-8 -*-

from odoo import fields, models

class Client(models.Model):
    _name = 'freelancer.client'
    _description = 'Client Information'

    name = fields.Char(string='Client Name', required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')],
        default='male'
    )
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    address = fields.Text(string='Address')
    project_ids = fields.One2many('freelancer.project', 'client_id', string='Projects')
    client_image = fields.Image(string='Image', max_width=1920, max_height=1920)
