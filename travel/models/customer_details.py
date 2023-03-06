from odoo import fields,models,api


class CustomerDetails(models.Model):
    _name="customer.details"
    _description="Customer Travel Details"
    
    name=fields.Char(string="Customer Name:",required=True)
    mob=fields.Integer(string="Mobile No.")
    address=fields.Char(string="Address")
    booking_no=fields.Integer(string="No. of Bookings",compute="_compute_booking_no")
    cust_booking_ids=fields.One2many('travel.booking','cust_detail_id')
    

    @api.depends('cust_booking_ids')
    def _compute_booking_no(self):
        for record in self:
            if record.cust_booking_ids:
                record.booking_no=len(record.cust_booking_ids)
            else:
                record.booking_no=0
