from odoo import models, fields

class MealCategory(models.Model):
    _name = "order.meal_category"
    _description = "Meal Category"
    _order = "code"

    name = fields.Char(string="Meal Category" , required=True , copy=False)
    code = fields.Char(string="Category Code",  required=True , copy=False)