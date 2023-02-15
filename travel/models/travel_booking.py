from odoo import models,fields,api

class TravelBooking(models.Model):
    _name="travel.booking"
    _description="Travel Bookings"

    
    name=fields.Char(string="Enter Your name:")
    
    country_id=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state_id=fields.Many2one('res.country.state',string='State',help='Select State',ondelete='restrict',compute="_compute_state_id",readonly=False)
    city=fields.Char(store=True)
    place_id=fields.Many2one('place.details',string="Select Place",store=True,readonly=False)

    @api.depends('country_id')
    def _compute_state_id(self):
            if self.country_id.id==self.state_id.country_id:
                self.state_id=self.state_id



   