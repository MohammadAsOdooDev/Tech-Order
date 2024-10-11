from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Order(models.Model):

    _name = "order.order"
    _description = "The Main Order Modle"

    _sql_constraints = [
        ("unique_order_name" , 'unique (name)' , 'Order name already exist')
    ]

    _ORDER_TYPE_SELECTION = [
        ("internal" , "Internal"),
        ("external" , "External")
    ]

    _ORDER_STATE_SELECTION = [
        ("draft"        , "Draft"),
        ("confirmed"    , "Confirmed"),
        ("in_process"   , "In Process"),
        ("cancelled"    , "Cancelled"),
        ("delivered"    , "Deliverd"),
    ]

    name = fields.Char(string="Order Name", required=True)
 
    type = fields.Selection(
        selection=_ORDER_TYPE_SELECTION , 
        string="Order Type" , 
        required=True , 
        index=True
    )
    date = fields.Date(
        string="Order Date" , 
        required=False , 
        default=fields.datetime.now().date() , 
    )
    state = fields.Selection(
        selection=_ORDER_STATE_SELECTION , 
        required=True , 
        index=True
    )

    is_urgent = fields.Boolean(string="Is Urgent" , default=False)
    table_number = fields.Integer(string="Table Number") 
    note = fields.Char(string="Note")
    total_price = fields.Float(
        string="Total price" , 
        readonly=True, 
        compute="_compute_total_price"
    )

    customer_id = fields.Many2one("res.partner" , string="Customer", required=True)


    item_ids = fields.One2many(
       comodel_name="order.order_item", 
       inverse_name="order_id",
       string="Related Items", 
       required=True,
    )
    order_tag_ids = fields.Many2many(
        comodel_name="order.order_tag" , 
        string="Tags",
    )
    external_item_ids = fields.Many2many(
        comodel_name="order.external_item",
        string="Related External Items"
    )


    @api.constrains("total_price")
    def _check_total_price(self):
        for order in self:
            if order.total_price < 0:
                raise ValidationError("Order total price should be positive")

    @api.constrains("date")
    def _check_date(self):
        for order in self:
            if order.date > datetime.now().date():
                raise ValidationError("Order date can't be in the future")

    @api.constrains("item_ids")
    def _check_item_ids(self):
        for order in self:
            if not len(order.item_ids):
                raise ValidationError("Order can't be created with no items")

    @api.depends("item_ids.total_price")
    def _compute_total_price(self):
        for order in self:
            if type(order.item_ids) is list or len(order.item_ids) > 0:
                for item in order.item_ids:
                    order.total_price += item.total_price
            else:
                order.total_price = 0
    