#-*- coding: utf-8 -*-

from odoo import fields, models

class Client(models.Model):
    _name = 'freelancer.client'
    _description = 'Client Information'

    name = fields.Char(string='Client Name', required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')]
    )
    email = fields.Char(string='Email', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    address = fields.Text(string='Address')
    projects = fields.One2many('freelancer.project', 'client_id', string='Projects')
