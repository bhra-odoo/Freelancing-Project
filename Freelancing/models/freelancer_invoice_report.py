#-*- coding: utf-8 -*-

from odoo import fields, models

class InvoiceReport(models.Model):
    _name = 'freelancer.invoice.report'
    _description = 'Invoice Report'

    name = fields.Char(string='Report Name', required=True)
    invoice_id = fields.Many2one('freelancer.invoice', string='Invoice', required=True)
    date = fields.Date(string='Report Date', required=True)
    description = fields.Text(string='Description')
