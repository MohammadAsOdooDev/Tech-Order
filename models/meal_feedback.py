from odoo import models, fields, api

class MealFeedback(models.Model):
    _name = "order.meal_feedback"
    _description = "Meal Feedback model"

    _RATE_SELECTION = [
        ("0" , "Bad"),
        ("1" , "Med."),
        ("2" , "Good")
    ]

    comment = fields.Text(
        string="Comment",
    )
    rate = fields.Selection(
        selection=_RATE_SELECTION , 
        string="Rate" , 
        required=True
    )

    meal_id = fields.Many2one(
        comodel_name="order.meal",
        string="Meal",
        required=True,
        ondelete="cascade"
    )
    customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        required=True,
        ondelete="cascade"
    )


