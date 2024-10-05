from odoo import models, fields

class Tag(models.Model):
    _name = "order.tag"
    _description = "Main Tag Model"
    _uid = "tag_id"

    name = fields.Char(string="Tag Name" , required=True , copy=True , trim=True)