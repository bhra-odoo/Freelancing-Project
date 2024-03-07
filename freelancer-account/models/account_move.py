#-*- coding: utf-8 -*-

from odoo import api, fields, models, Command

class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'

    freelancer_id = fields.Many2one('freelancer.freelancer', string='Username')
    user_id = fields.Many2one('res.users', string='Customer')
    