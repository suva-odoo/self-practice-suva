from odoo import fields,models


class TravelPlaceTypes(models.Model):
    _name="travel.place.types"
    _description="Travel Place Types"

    name=fields.Char(string="Place Type",required=True)