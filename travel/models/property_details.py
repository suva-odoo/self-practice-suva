from odoo import models,fields

class PropertyDetails(models.Model):
    _name="property.details"
    _description="Property Details"
     

    location=fields.Char("Location",required=True)
    bedrooms=fields.Integer("Bedrooms")
    bathrooms=fields.Integer("Bathrooms")
    no_of_guests=fields.Integer("Guests")

    

    

