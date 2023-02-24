
from odoo import fields,models,api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta


class HostDetails(models.Model):
    _name="host.details"
    _description="Host Details"


    name=fields.Char(required=True)
    email=fields.Char(required=True)
    mob=fields.Integer(required=True)
    date_of_birth=fields.Date()
    age=fields.Integer(compute="_compute_age",store=True)
    image=fields.Binary(string="Upload your image")
    address=fields.Char()
    places_owned=fields.Integer(string="Places Owned",compute="_compute_places_owned",store=True)
    place_ids=fields.One2many('place.details','host_id',string="Places")
    
    
    @api.depends('place_ids.host_email')
    def _compute_places_owned(self):
        for rec in self:
              if rec.email:
                rec.places_owned=self.env['place.details'].search_count([('host_email','=',rec.email)])
     
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                dt=rec.date_of_birth
                d1=datetime.strptime(str(dt),"%Y-%m-%d").date()
                d2=date.today()
                rd=relativedelta(d2,d1)
                rec.age=str(rd.years)


         


