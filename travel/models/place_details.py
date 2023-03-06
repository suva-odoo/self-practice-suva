from odoo import models,fields,api
from datetime import datetime,date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError

class PlaceDetails(models.Model):
    _name="place.details"
    _description="Place Details"

    name=fields.Char(required=True)
    
    
 #city_id = fields.Many2one('res.country.state.city', "CityID") 
 #city =  fields.Char(related='city_id.name', "City") 
  
    host_id=fields.Many2one('host.details',string="Host")
   
    host_name=fields.Char(related="host_id.name")
    host_email=fields.Char(related="host_id.email")
    mob=fields.Integer(related="host_id.mob")
    description=fields.Text()
    country_id = fields.Many2one('res.country', string='Country',store=True,ondelete="restrict")
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]",store=True,ondelete="restrict")
    city_id=fields.Many2one('res.city',domain="[('state_id', '=?', state_id)]")
    #city=fields.Char(string="City",help="Enter City",required="True")
    landmark=fields.Char(string="Any Landmark")
    rent=fields.Integer()
    beds=fields.Integer(string="Beds")
    bedrooms=fields.Integer(string='Bedrooms')
    bathrooms=fields.Integer(string='Bathrooms')
    no_of_guests=fields.Integer(string='Guests')
    description=fields.Text()
    facilites_ids=fields.Many2many('travel.facilites')

    available=fields.Boolean()
    
    state=fields.Selection(string="Status",default="available",

                         selection=[
                            ('available','Available'),
                            ('not_available','Not Available')
                          
                           ])

    add_vehicle_line_ids=fields.One2many('travel.transport','vehicle_id',string="Select vehicle")
    place_type_id=fields.Many2one('travel.place.types',string="Place Type")    
   #  place_type=fields.Char(related="place_type_id.name",string="Place")
    
    booking_ids=fields.One2many('travel.booking','travel_booking_id')
   #  booked_from=fields.Date()
   #  booked_to=fields.Date()
    

    
    
  



   


