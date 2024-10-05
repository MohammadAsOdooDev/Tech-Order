from odoo import models, fields, api

class Item(models.Model):

    _name = "order.item"
    _description = "Order Item Model"

    quantity = fields.Integer(string="Quantity" , required=True, copy=True)
    price = fields.Float(string="Price(Per Item)", required=True, copy=True)

    total_price = fields.Float(string="Total Price", compute="_compute_total_price")


    @api.depends("price")
    @api.depends("quantity")
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.quantity * record.price