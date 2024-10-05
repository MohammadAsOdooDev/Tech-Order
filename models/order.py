from odoo import models, fields

class Order(models.Model):
    _name = "order.order"
    _description = "The Main Order Modle"

    ORDER_TYPE_SELECTION = [
        ("internal" , "Internal"),
        ("external" , "External")
    ]

    ORDER_STATE_SELECTION = [
        ("draft"        , "Draft"),
        ("confirmed"    , "Confirmed"),
        ("in_process"   , "In Process"),
        ("cancelled"    , "Cancelled"),
        ("delivered"    , "Deliverd"),
    ]

    name = fields.Char(string="Order Name", required=True)
    
    type = fields.Selection(
        selection=ORDER_TYPE_SELECTION , 
        string="Order Type" , 
        required=True , 
        index=True
    )
    
    date = fields.Date(string="Order Date" , required=True)
    state = fields.Selection(selection=ORDER_STATE_SELECTION , required=True , index=True)

    total_price = fields.Float(string="Total price" , required=True)
    note = fields.Char(string="Note")

    is_urgent = fields.Boolean(string="Is Urgent" , default=False)

    # item_ids = fields.One2many("order.item", string="Related Items")

    order_tag_ids = fields.Many2many(
        comodel_name="order.tag" , 
        string="Tags"
    )
