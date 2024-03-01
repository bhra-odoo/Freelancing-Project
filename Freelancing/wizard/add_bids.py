#-*- coding: utf-8 -*-

from odoo import fields, models

class AddBids(models.TransientModel):
    _name = 'add.bids'
    _description = 'Add Bids to project'

    project_id = fields.Many2one('freelancer.project', string='Project', ondelete='cascade')
    freelancer_id = fields.Many2one('freelancer.freelancer', string='Freelancer')
    bid_amount = fields.Float(string='Bid Amount')
    bid_description = fields.Text(string='Bid Description')

    def action_add_bid(self):
        active_ids = self.env.context.get('active_ids')
        projects = self.env['freelancer.project'].browse(active_ids)
        for project in projects:
            project.bid_ids.create(
                {
                    'bid_amount': self.bid_amount,
                    'bid_description': self.bid_description,
                    'freelancer_id': self.freelancer_id.id,
                    'project_id': project.id,
                }
            )
            