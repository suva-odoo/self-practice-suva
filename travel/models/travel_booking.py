from odoo import models,fields,api
from datetime import datetime,date,time,timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError,ValidationError

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"
    _inherit=['mail.thread','mail.activity.mixin']
  

   
    
    cust_id=fields.Many2one('customer.details',string="Name:",store=True)
    mob=fields.Integer(string="Mobile No.",related="cust_id.mob")
    address=fields.Char(string="Address",related="cust_id.address")

    
    
    
    travel_booking_id=fields.Many2one('place.details',store=True,readonly=False,compute="_compute_travel_booking_id")
    place_name=fields.Char(related="travel_booking_id.name")
    

    country_id = fields.Many2one('res.country', string='Country',store=True)
    state_id = fields.Many2one("res.country.state", string='State', domain="[('country_id', '=?', country_id)]",store=True)
    
    # city=fields.Char(store=True)
    city_id=fields.Many2one('res.city',domain="[('state_id', '=?', state_id)]",store=True)
    place_id=fields.Many2one('place.details',string="Select Place",store=True,readonly=False,domain="[('country_id','=',country_id),('state_id','=',state_id),('city_id','=',city_id)]")
    
    #place_booking=fields.Char(related="place_id.name")
    place_type=fields.Many2one(string="Place Type",related="place_id.place_type_id")
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
      default="inquiry",
      copy=False,
      tracking=True

    )

    available=fields.Boolean()   
    book_from=fields.Date()
    book_to=fields.Date()
    days=fields.Integer(compute='_compute_days',store=True)  
    total=fields.Float(string="Total amount to pay",store=True,compute="_compute_total")
    cust_detail_id=fields.Many2one('customer.details',compute="_compute_cust_detail_id",store=True)
    
     
    @api.depends('cust_id')
    def _compute_cust_detail_id(self):
          for record in self:
             if record.cust_id:
                record.cust_detail_id=record.cust_id
             else:
                record.cust_id=record.cust_detail_id

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

    @api.depends('place_id')
    def _compute_travel_booking_id(self):
        for record in self:
            if record.place_id:
                record.travel_booking_id=record.place_id
                
            else:
               record.place_id=record.travel_booking_id            
    
    def action_book(self):
     for record in self:
        record.state="booked"
     
    def action_cancel(self):
      for record in self:
        record.state="cancel" 

    


    @api.model
    def create(self,vals):
          count= self.env['place.details'].browse(vals["place_id"])
          for c in count.booking_ids:
             book_from=c.book_from
             book_to=c.book_to
             d=book_from - book_to
             
             for i in range(d.days+1):
                day=book_from+timedelta(days=i)
                if vals['book_from'] == day or vals["book_to"] == day:
                   raise UserError("You cannot book on selcted date")
                
    
          return super(TravelBooking,self).create(vals)
       
        # count= self.env['estate.property'].browse(vals["property_id"])

    # @api.constrains('book_from','book_to')
    # def check_date(self):
    #     count=1
    #     for rec in self:
    #       for record in self.place_id.booking_ids:
    #           count=count+1
    #           v=len(self.place_id.booking_ids)-1
    #           d1=record.book_from
    #           d2=record.book_to
    #           d=d2-d1
    #           for i in range(d.days+1):
    #            day=d1+timedelta(days=i)
    #            if count <= v and (rec.book_from == day or rec.book_to == day):
    #              raise UserError("Error")



   
    
                  # print("Hello rec.book_from"+str(rec.book_from))
                  # print("World rec.book_to"+str(rec.book_to))
                  # print("Days:" +str(day))
                               


    






    # @api.constrains('book_from','book_to')
    # def check_date(self): 
    #     for record in self:  
    #         if self.env['travel.booking'].search_count(['&',('place_name','=',record.place_name),'|',('book_from','<=',record.book_to),('book_from','=',record.book_from),('book_to','=',record.book_to)])>1:
    #           raise UserError("You cannot book on selected date")

            
# book_from = new_book_from | book_to > new _book_to
# book_from < new_book_from | book_to = new_book_to
# book_from < new_book_from | book_to < new_book_to
# book_from > new_book_from | book_to > new_book_from


              # if self.env['travel.booking'].search_count(['&',('place_name','=',record.place_name),'|','|',('book_from','=',record.book_from),('book_to','=',record.book_to),'|','&',('book_from','=',record.book_from),('book_to','>=',record.book_to),'|','&',('book_from','=',record.book_from),('book_to','<=',record.book_to),'&','&',('book_from','<',record.book_from),('book_to','<=',record.book_to),('book_to','>=',record.book_from)])>1:


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




        
       
    
      
        
  




