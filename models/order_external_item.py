from odoo import models, api, fields
from odoo.exceptions import ValidationError

class OrderExtenralItem(models.Model):
    _name = "order.external_item"
    _description = "Order's External Item Model"

    product_id = fields.Many2one("order.product" , string="Related Product" , required=True)


