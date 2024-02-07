from odoo import fields, models

class Customer(models.Model):
    _name = "customer"

    name = fields.Char("Customer Name")
    phone_no = fields.Integer("Phone Number")
    gender = fields.Selection([('male','Male'),('female','Female')])
    email = fields.Text("Email")
    address = fields.Text("Customer Address")
    dob = fields.Date("Date Of Birth")
    image = fields.Image()
