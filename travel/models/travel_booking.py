from odoo import models,fields,api

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    
    name=fields.Char(string="Enter Your name:")
    
    country_id=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state_id=fields.Many2one('res.country.state',string='State',store=True,help='Select State',ondelete='restrict')
    city=fields.Char()
    place_id=fields.Many2one('place.details',string="Select Place")

    @api.onchange('country_id')
    def set_values_to(self):
        if self.country_id:
            ids=self.env['res.country.state'].search([('country_id','=',self.country_id.id)])
            return{
                'domain':{'state_id':[('id','in',ids.ids)],}
            }

    @api.onchange('country_id','state_id','city')
    def set_value_place(self):
        if self.country_id:
            return { 'domain':{'place_id':[('country_id','=',self.country_id.id),('state_id','=',self.state_id.id),('city','=',self.city)]}}
    



   