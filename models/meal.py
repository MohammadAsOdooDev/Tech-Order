from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Meal(models.Model):
    _name= "order.meal"     
    _description= "Order Meal"  

    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", required=True , copy=False)

    category_id = fields.Many2one(
        comodel_name="order.meal_category", 
        inverse_name="category_code",
        string="Meal Cat." , 
        ondelete="set null"
    )

    @api.constrains("price")
    def _check_price(self):
        for meal in self:
            if meal.price <= 0:
                raise ValidationError("Meal price should be larger than zero")