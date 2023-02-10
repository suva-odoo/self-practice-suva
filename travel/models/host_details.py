
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
    age=fields.Integer(readonly=True)
    image=fields.Binary(string="Upload your image")
    address=fields.Char()
    places_owned=fields.Integer(string="Places Owned",compute="_compute_places_owned")

    def _compute_places_owned(self):
        for rec in self:
            rec.places_owned=self.env['place.details'].search_count([('host_email','=',rec.email)])

    

     
    @api.onchange('date_of_birth')
    def set_age(self):
        for rec in self:
            if rec.date_of_birth:
                dt=rec.date_of_birth
                d1=datetime.strptime(str(dt),"%Y-%m-%d").date()
                d2=date.today()
                rd=relativedelta(d2,d1)
                rec.age=str(rd.years)


         
            