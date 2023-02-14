from odoo import models,fields,api
from datetime import datetime,date
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import UserError

class PlaceDetails(models.Model):
    _name="place.details"
    _description="Place Details"

    name=fields.Char(required=True)
    host_name=fields.Char()
    host_email=fields.Char()
    description=fields.Text()
    country_id=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state_id=fields.Many2one('res.country.state',string='State',store=True,help='Select State',ondelete='restrict')
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
    add_vehicle_line_ids=fields.One2many('travel.transport','vehicle_id',string="Select vehicle")
    

    @api.onchange('booked_from')
    def compute_booked_from(self):
        if datetime.strptime(str(self.booked_from),DEFAULT_SERVER_DATE_FORMAT).date() <datetime.now().date():
           self.booked_from = False
           return {'warning': {
                    'title': "Warning",
                    'message': "Please select current or future date",
                    }
                }
                 
    @api.onchange('booked_to')
    def compute_booked_to(self):  
        dt1=datetime.strptime(str(self.booked_from),DEFAULT_SERVER_DATE_FORMAT).date()
        dt2=datetime.strptime(str(self.booked_to),DEFAULT_SERVER_DATE_FORMAT).date()
        if dt2 < dt1:
            self.booked_to = False
            return {'warning': {
                    'title': "Warning",
                    'message': "Please select appropriate date",
                    }
                }
 
    
    @api.onchange('country_id')
    def set_values_to(self):
        if self.country_id:
            return { 'domain':{'state_id':[('country_id','=',self.country_id.id)]}}
        else:
            return {'domain':{'state_id':[]}}



   


