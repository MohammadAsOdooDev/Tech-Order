from odoo import models , fields

class Meal(models.Model):
    _name= "order.meal"     # technical name for the model (module-level uniqueness)
    _description= "Order Meal"  # description name

    name = fields.Char(string="Name", required=True)
    price = fields.Float(string="Price", required=True , copy=False)

    category_id = fields.Many2one(
        comodel_name="order.meal_category", 
        inverse_name="category_code",
        string="Meal Cat." , 
        ondelete="set null"
    )
