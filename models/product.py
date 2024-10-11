from odoo import models, fields

class Product(models.Model):
    _description = "Custom Products Model"
    _inherit = "product.product"

    product_description = fields.Text(string="Description" , required=False , copy=True)