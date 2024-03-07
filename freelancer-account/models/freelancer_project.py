#-*- coding: utf-8 -*-

from odoo import api, fields, models, Command

class FreelancerProject(models.Model):
    _inherit = 'freelancer.project'

    def action_completed(self):
        print("Custom action_sold method called")
        move_obj = self.env['account.move']
        for project_rec in self:

            total_price = project_rec.ammount
            tax_amount = total_price * 0.15
            platform_fees = 100.00

            vals = {
                'partner_id': project_rec.assigned_to.user_id.id,
                'freelancer_id': project_rec.assigned_to.id,
                'move_type': 'out_invoice',
                'invoice_line_ids': [
                    Command.create({
                        'name': 'Total Project Amount',
                        'quantity': 1,
                        'price_unit': total_price
                    }),
                    Command.create({
                        'name': 'Tax (15%)',
                        'quantity': 1,
                        'price_unit': tax_amount
                    }),
                    Command.create({
                        'name': 'Platform Fees',
                        'quantity': 1,
                        'price_unit': platform_fees
                    }),
                ]
            }
            move_obj.create(vals)

        return super().action_completed()
    