#-*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

class FreelancerBids(models.Model):
    _name = 'freelancer.bids'
    _description = 'Freelancer Bids'

    freelancer_id = fields.Many2one('freelancer.freelancer', string='Freelancer')
    project_id = fields.Many2one('freelancer.project', string='Project', ondelete='cascade')
    bid_amount = fields.Float(string='Bid Amount')
    bid_description = fields.Text(string='Bid Description')
    status = fields.Selection([('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', string='Status')

    def action_offer_accepted(self):
        if self.project_id.state != 'offer_accepted':
            self.project_id.write({
                'state': 'offer_accepted',
                'assigned_to': self.freelancer_id,
                'ammount': self.bid_amount
            })
            self.status = 'accepted'
            other_offers = self.project_id.bid_ids.filtered(lambda bid: bid.id != self.id)
            other_offers.write({'status': 'refused'})
        else:
            raise UserError("Another ofer is alrealy accepted")

    def action_offer_refused(self):
        self.status = 'rejected'

    @api.model
    def create(self, vals):
        if 'project_id' in vals:
            self.project_obj.state = 'offer_received'
            return super(FreelancerBids, self).create(vals)
        else:
            raise ValidationError("Project ID is required for creating a bid.")
