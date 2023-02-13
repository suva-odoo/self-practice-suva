from odoo import models,fields,api

class TravelTransport(models.Model):
    _name="travel.transport"
    _description="Travel Transportation"

    vehicle_name=fields.Char(string="Vehicle Name",required=True)
    capacity=fields.Integer(string="Capacity",required=True)
    rent=fields.Float(string="Rent",required=True)
    description=fields.Text(string="Description")
    vehicle_image=fields.Image(string="Upload Vehicle Image")
