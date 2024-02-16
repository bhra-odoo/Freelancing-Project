#-*- coding: utf-8 -*-

from odoo import fields, models

class Project(models.Model):
    _name = 'freelancer.project'
    _description = 'Freelance Project'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    client_id = fields.Many2one('freelancer.client', string='Client', required=True, ondelete='cascade')
    assigned_to = fields.Many2one('freelancer.freelancer', string='Assigned To')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    task_ids = fields.One2many('freelancer.task', 'project_id', string='Tasks', required=True)
    tag_ids = fields.Many2many('freelancer.tags', string='Tags')
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', required=True, default="new", copy=False)
