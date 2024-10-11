from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OrderItem(models.Model):

    _name = "order.order_item"
    _description = "Order Item Model"
    _rec_name = "item_code"

    _sql_constraints = [
        ('unique_item_code' , 'unique (item_code)' , 'Item code should be unique')
    ]

    item_code = fields.Char(string="Item Code" , required=True)
    quantity = fields.Integer(string="Quantity" , required=True, copy=True)
    price = fields.Float(string="Price(Per Item)", readonly=True , compute="_compute_item_price")

    total_price = fields.Float(
        string="Total Price", 
        compute="_compute_total_price", 
        store=True
    )

    order_id = fields.Many2one(
        comodel_name="order.order", 
        required=True, 
        string="Related Order",
    )
    meal_id = fields.Many2one(
        comodel_name="order.meal", 
        required=True , 
        string="Related Meal" , 
    )

    @api.model
    def _create(self, data_list):
        item = super()._create(data_list)
        item.item_code = f"{item.order_id.name}-{item.item_code}"

    @api.depends("price")
    @api.depends("quantity")
    def _compute_total_price(self):
        for item in self:
            item.total_price = item.quantity * item.price

    @api.depends("price")
    @api.depends("meal_id.price")
    def _compute_item_price(self):
        for item in self:
            item.price = item.meal_id.price


    @api.constrains("price")
    def _check_price(self):
        for item in self:
            if item.price <= 0:
                raise ValidationError(
                    f"Item ({self.item_code}): price should be larger than zero"
                )

    @api.constrains("total_price")
    def _check_total_price(self):
        for item in self:
            if item.total_price <= 0:
                raise ValidationError(
                    f"Item ({self.total_price}): total price should be larger than zero"
                )


    @api.constrains("quantity")
    def _check_quantity(self):
        for item in self:
            if item.quantity <= 0:
                raise ValidationError(
                    "Item ({}): Quantity should be larger than zero"
                    .format(item.item_code)
                )

    @api.constrains("order_id")
    def _check_order_id(self):
        for item in self:
            if len(item.order_id) != 1:
                raise ValidationError(
                    "Item ({}) should belong to only one order"
                    .format(item.item_code)
                )
            
