from odoo import models,fields,api
from datetime import datetime,date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    
    name=fields.Char(string="Enter Your name:")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")
    
    city=fields.Char(store=True)
    book_from=fields.Date()
    book_to=fields.Date(compute="_compute_book_from",readonly=False,store=True)
    place_id=fields.Many2one('place.details',string="Select Place",store=True,readonly=False,domain="[('country_id','=',country_id),('state_id','=',state_id),('city','=',city)]")
    place_type=fields.Char(string="Place Type",related="place_id.place_type")

    
    

    @api.depends("book_from")
    def _compute_book_from(self):
      for record in self:
         if record.book_from:
           if datetime.strptime(str(record.book_from),DEFAULT_SERVER_DATE_FORMAT).date() < datetime.now().date():
              record.book_from=False
              raise UserError("error")
                     
          


        
       
         
      
        

  




