from odoo import models,fields,api

class TravelTransport(models.Model):
    _name="travel.transport"
    _description="Travel Transportation"
    _rec_name="vehicle_name"

    vehicle_id=fields.Many2one('place.details',required=True)
    vehicle_name=fields.Char(string="Vehicle Name")
    capacity=fields.Integer(string="Capacity",required=True)
    rent=fields.Float(string="Rent",required=True)
    description=fields.Text(string="Description")
    vehicle_image=fields.Image(string="Upload Vehicle Image")
