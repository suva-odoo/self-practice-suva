from odoo import models,fields,api
from datetime import datetime,date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError,ValidationError

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    
    name=fields.Char(string="Enter Your name:")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")
    
    city=fields.Char(store=True)
    book_from=fields.Date(readonly=False)
    book_to=fields.Date(readonly=False)
    place_id=fields.Many2one('place.details',string="Select Place",store=True,readonly=False,domain="[('country_id','=',country_id),('state_id','=',state_id),('city','=',city)]")
    place_type=fields.Char(string="Place Type",related="place_id.place_type")
    travel_facilites_ids=fields.Many2many(related="place_id.facilites_ids")    
    bedrooms=fields.Integer(string="Bedrooms",related="place_id.bedrooms")
    beds=fields.Integer(string="Beds",related="place_id.beds")
    no_of_guests=fields.Integer(string="Maximum Guests",related="place_id.no_of_guests")
    bathrooms=fields.Integer(string="Bathrooms",related="place_id.bathrooms")
    description=fields.Text(string="Description",related="place_id.description")
    transportation_ids=fields.One2many(related="place_id.add_vehicle_line_ids")   
    rent=fields.Integer(string="Place Rent",related="place_id.rent")

    state=fields.Selection(
      selection=[
        ('inquiry','Inquiry'),
        ('payment','Payment'),
        ('booked','Booked'),
        ('cancel','Cancelled')

      ],
      copy=False

    )
   
    total=fields.Float(string="Total amount to pay",compute="_compute_total")


    @api.depends("transportation_ids.rent","place_id.rent")
    def _compute_total(self):
      for record in self:
        record.total=record.transportation_ids.rent + record.place_id.rent   
    



        
       
    
      
        
  




