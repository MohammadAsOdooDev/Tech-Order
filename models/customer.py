from odoo import models, fields

class Customer(models.Model):
    _inherit = "res.partner"

    customer_rank = fields.Integer(string="Rank" , required=True , copy=True)