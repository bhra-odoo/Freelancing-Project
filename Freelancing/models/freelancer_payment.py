#-*- coding: utf-8 -*-

from odoo import fields, models

class Payment(models.Model):
    _name = 'freelancer.payment'
    _description = 'Invoice Payment'

    name = fields.Char(string='Payment Reference', required=True)
    invoice_id = fields.Many2one('freelancer.invoice', string='Invoice', required=True)
    date = fields.Date(string='Payment Date', required=True)
    amount = fields.Float(string='Amount', defalt=0, required=True)
    payment_method = fields.Selection([
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
        ('other', 'Other')
    ], string='Payment Method', required=True)
