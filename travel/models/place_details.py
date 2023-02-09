from odoo import models,fields,api

class PlaceDetails(models.Model):
    _name="place.details"
    _description="Place Details"

    name=fields.Char(required=True)
    description=fields.Text()
    country=fields.Many2one('res.country',string='Country',required=True,help='Select Country',ondelete='restrict')
    state=fields.Many2one('res.country.state',string='State',store=True,help='Select State',ondelete='restrict')
    
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
    
 

  
    @api.onchange('country')
    def set_values_to(self):
        if self.country:
            ids=self.env['res.country.state'].search([('country_id','=',self.country.id)])
            return{
                'domain':{'state':[('id','in',ids.ids)],}
            }
   


