from odoo import fields, models

class ServiceProvider(models.Model):
    _name = "service.providers"

    name = fields.Char()
    description = fields.Text()
    phone_no = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female')])
    email = fields.Text()
    address = fields.Text()
    dob = fields.Date()
    work = fields.Char()
    image = fields.Image()
