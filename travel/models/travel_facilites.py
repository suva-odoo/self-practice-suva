from odoo import models,fields

class TravelFacilites(models.Model):
    _name="travel.facilites"
    _description="Travel Facilites"

    name=fields.Char(string="Facilites",required=True)
