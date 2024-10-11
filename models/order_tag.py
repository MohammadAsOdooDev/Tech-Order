from odoo import models, fields

class OrderTag(models.Model):
    _name = "order.order_tag"
    _description = "Order Tag Model"

    name = fields.Char(string="Tag Name" , required=True , copy=True , trim=True)
    color = fields.Integer(string="Color")