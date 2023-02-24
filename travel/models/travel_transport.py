from odoo import models,fields,api

class TravelTransport(models.Model):
    _name="travel.transport"
    _description="Travel Transportation"
    _rec_name="vehicle_name"

    vehicle_id=fields.Many2one('place.details',compute="compute_vehicle_id",store=True)
    vehicle_name=fields.Char(string="Vehicle Name")
    capacity=fields.Integer(string="Capacity",required=True)
    rent=fields.Float(string="Rent",required=True,default=0)

    description=fields.Text(string="Description")
    vehicle_image=fields.Image(string="Upload Vehicle Image")
    
    place_id=fields.Many2one('place.details')

    place_name=fields.Char(related="vehicle_id.name")
   
    status=fields.Selection(
        
        selection=[('include','Included'),('not include','Not included')]
    )
    

    @api.depends('place_id')
    def compute_vehicle_id(self):
        for record in self:
            if record.place_id:
                record.vehicle_id=record.place_id

            else:
                record.place_id=record.vehicle_id
     


    def action_accept(self):
        for record in self:
            record.status="include"

    def action_refuse(self):
        for record in self:
            record.status="not include"