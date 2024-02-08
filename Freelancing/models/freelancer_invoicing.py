#-*- coding: utf-8 -*-

from odoo import fields, models

class Invoice(models.Model):
    _name = 'freelancer.invoice'
    _description = 'Freelancer Invoice'

    name = fields.Char(string='Freelancer', required=True)
    project_id = fields.Many2one('freelancer.project', string='Project', required=True)
    client_id = fields.Many2one('freelancer.client', string='Client', required=True)
    date = fields.Date(string='Invoice Date', required=True)
    due_date = fields.Date(string='Due Date', required=True)
    amount_total = fields.Float(string='Total Amount', default=0, required=True)
