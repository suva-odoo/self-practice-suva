from odoo import models,fields,api
from datetime import datetime,date,time
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError,ValidationError

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    
    name=fields.Char(string="Enter Your name:")
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]")
    
    # city=fields.Char(store=True)
    city_id=fields.Many2one('res.city',domain="[('state_id', '=?', False)]")
    place_id=fields.Many2one('place.details',string="Select Place",store=True,readonly=False,domain="[('country_id','=',country_id),('state_id','=',state_id),('city_id','=',city_id)]")
    place_type=fields.Char(string="Place Type",related="place_id.place_type")
    travel_facilites_ids=fields.Many2many(related="place_id.facilites_ids")    
    bedrooms=fields.Integer(string="Bedrooms",related="place_id.bedrooms")
    beds=fields.Integer(string="Beds",related="place_id.beds")
    no_of_guests=fields.Integer(string="Maximum Guests",related="place_id.no_of_guests")
    bathrooms=fields.Integer(string="Bathrooms",related="place_id.bathrooms")
    description=fields.Text(string="Description",related="place_id.description")
   # transportation_ids=fields.One2many(related="place_id.add_vehicle_line_ids")   
    rent=fields.Integer(string="Place Rent",related="place_id.rent")
    transportation_ids=fields.Many2one('travel.transport',domain="[('vehicle_id', '=?',place_id)]")
    transport_capacity=fields.Integer(related="transportation_ids.capacity")
    transport_rent=fields.Float(related="transportation_ids.rent")
    state=fields.Selection(
      selection=[
        ('inquiry','Inquiry'),
        ('payment','Payment'),
        ('booked','Booked'),
        ('cancel','Cancelled')

      ],
      copy=False

    )
   
    book_from=fields.Date()
    book_to=fields.Date()
    days=fields.Integer(compute='_compute_days',store=True)  
    total=fields.Float(string="Total amount to pay",compute="_compute_total")

 

    @api.depends('book_from','book_to')
    def _compute_days(self):
      for record in self:
        if record.book_from and record.book_to:
          record.days=(record.book_to - record.book_from).days + 1


    @api.depends('transport_rent','rent','days')
    def _compute_total(self):
      for record in self:
        record.total=(record.rent +record.transport_rent)* record.days

    @api.constrains('book_from')
    def _check_book_from(self):
        for record in self:
            if record.book_from < datetime.date(datetime.today()):
               raise ValidationError("Please select appropriate date")

  
    

            

       
          # if record.book_from:
          #   start=record.book_from
          #   end=time.strftime('%Y-%m-%d')
          #   if start and end:
          #      if start < end:
          #       raise UserError("Error")
          #   return True




 

            # if datetime.strptime(str(record.book_from),"%Y-%m-%d").date() < datetime.today.date():
            #  raise UserError("Please select appropriate date")
             
       # if dt1 < datetime.now.date():
        #   raise UserError("Please select the appropriate date")




        
       
    
      
        
  




