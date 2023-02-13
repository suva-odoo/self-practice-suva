from odoo import models,fields,api

class PlaceDetails(models.Model):
    _name="place.details"
    _description="Place Details"

    name=fields.Char(required=True)
    host_name=fields.Char()
    host_email=fields.Char()
    description=fields.Text()
    country=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state=fields.Many2one('res.country.state',string='State',store=True,help='Select State',ondelete='restrict')
    city=fields.Char(string="City",help="Enter City",required="True")
    landmark=fields.Char(string="Any Landmark")
    rent=fields.Integer()
    beds=fields.Integer(string="Beds")
    bedrooms=fields.Integer(string='Bedrooms')
    bathrooms=fields.Integer(string='Bathrooms')
    no_of_guests=fields.Integer(string='Guests')
    description=fields.Text()
    swim_pool=fields.Boolean(string="Swimming Pool")
    wifi=fields.Boolean(string="Wi-Fi")
    tv=fields.Boolean(string="TV")
    cooking=fields.Boolean(string="Cooking")
    washer=fields.Boolean(string="Washing")
    booked_from=fields.Date()
    booked_to=fields.Date()
    add_vehicle_lines=fields.One2many('test.b','connect_test_b',string="Select Vehicle")
    
    class TestB(models.Model):
        _name="test.b"
        _description="Transportation"
        connect_test_b=fields.Many2one('place.details',string="Connect")
        vehicle_name=fields.Many2one('travel.transport',string="Select vehicle")
        capacity=fields.Integer(string="Capacity",related="vehicle_name.capacity")
        rent=fields.Float(string="Rent",related="vehicle_name.rent")
     
    
    
    
  
  
    @api.onchange('country')
    def set_values_to(self):
        if self.country:
            return { 'domain':{'state':[('country_id','=',self.country.id)]}}
        else:
            return {'domain':{'state':[]}}



   


