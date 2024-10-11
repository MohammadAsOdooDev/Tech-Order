from odoo import models, api, fields
from odoo.exceptions import ValidationError

class Ingredient(models.Model):
    _name = "order.ingredient"
    _description = "Ingredient Model"

    name = fields.Char(string="Ingredient Name" , required=True)
    quantity = fields.Integer(string="Quantity", required=True)

    product_id = fields.Many2one(string="Related Product" , comodel_name="order.product", required=True)
    meal_id = fields.Many2one(string="Related Meal" , comodel_name="order.meal")

    @api.constrains("quantity")
    def _check_quantity(self):
        for ingredient in self:
            if ingredient.quantity <= 0:
                raise ValidationError("Ingredient quantity should be larger than zero")
