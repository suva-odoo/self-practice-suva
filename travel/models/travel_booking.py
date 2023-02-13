from odoo import models,fields,api

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    country=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state=fields.Many2one('res.country.state',string='State',store=True,help='Select State',ondelete='restrict')
    places=fields.Many2one('place.details',string="S")

    @api.onchange('country')
    def set_values_to(self):
        if self.country:
            ids=self.env['res.country.state'].search([('country_id','=',self.country.id)])
            return{
                'domain':{'state':[('id','in',ids.ids)],}
            }

   