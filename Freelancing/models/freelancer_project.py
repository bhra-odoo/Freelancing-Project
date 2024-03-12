#-*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class Project(models.Model):
    _name = 'freelancer.project'
    _inherit = ['mail.thread']
    _description = 'Freelance Project'

    name = fields.Char(string='Project Name', required=True)
    description = fields.Text(string='Description')
    client_id = fields.Many2one('freelancer.client', string='Client', required=True, ondelete='cascade')
    assigned_to = fields.Many2one('freelancer.freelancer', string='Assigned To')
    user_id = fields.Many2one(related='assigned_to.user_id')
    image = fields.Image(related='client_id.client_image')
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    task_ids = fields.One2many('freelancer.task', 'project_id', string='Tasks', required=True)
    tag_ids = fields.Many2many('freelancer.tags', string='Tags')
    ammount = fields.Float(string="Ammount")
    color = fields.Integer(string='Color')
    bid_ids = fields.One2many('freelancer.bids', 'project_id', string='Bids')
    bid_count = fields.Integer(string='Total Bids')
    task_count = fields.Integer(string='Total Tasks', compute='_compute_total_tasks', store=True)
    label_tasks = fields.Char(string='Use Tasks as', default='Tasks')
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ], string='State', required=True, default="new", copy=False)

    @api.depends('task_ids')
    def _compute_total_tasks(self):
        for record in self:
            record.task_count = len(record.task_ids)

    def action_completed(self):
        if self.state == 'canceled':
            raise UserError("Cannot Mark a Project Completed that is already Cnceled!")
        if all(task.status == 'completed' for task in self.task_ids):
            self.state = 'completed'
        else:
            raise UserError("You need to Complete Remaining Tasks!")
    
    def action_cancel(self):
        if self.state == 'completed':
            raise UserError("Cannot Mark a Project Canceled that is already Completed!")
        self.state = 'canceled'
    