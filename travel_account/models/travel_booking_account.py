from odoo import models,fields

class TravelBookingAccount(models.Model):
    _inherit="travel.booking"

    def action_book(self):
     for record in self:
          self.env["account.move"].create(
               {
                 "partner_id":record.travel_booking_id.host_id.id,
                 "move_type":"out_invoice",
                 "line_ids":[
                    (0,0,
                     {
                        'name':record.cust_id.name,
                        'price_unit':record.total,
    
                     })
                 ]
               }
          )
         
         
        
          return super().action_book()