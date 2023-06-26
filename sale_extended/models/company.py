
# -*- coding: utf-8 -*-
from odoo import api, fields, models




class ResCompany(models.Model):
    _inherit = 'res.company'

    bank_id = fields.Many2one('res.bank', string="Bank")
    
    customer = fields.Char(string="Customer")
    customer_mobile = fields.Char(string="Mobile")
    customer_email = fields.Char(string="Email")
    
    ho_name = fields.Char(string="Head Office Name")
    ho_address = fields.Char(string="Address")
    location = fields.Char(string="City")

    rc_no = fields.Char(string="RC/CAC No")
    vat_no = fields.Char(string="VAT No")
    tin_no = fields.Char(string="TIN NO.")

class ResBank(models.Model):
    _inherit = 'res.bank'

    acc_name = fields.Char(string="Account Name")
    acc_no = fields.Char(string="Account Number")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    special_instruction = fields.Html(string="Special Instruction")
    client_name = fields.Char(string="Client Name")
    client_mobile = fields.Char(string="Client Mobile Number")

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float(compute='_compute_disc_total',store=True)

    @api.depends('product_uom_qty','price_unit','discount')
    def _compute_disc_total(self):
        for disc in self:
            if disc.discount:
                disc.discount_amount = (disc.product_uom_qty * disc.price_unit * disc.discount)/100
            else:
                disc.discount_amount = 0




class AccountMove(models.Model):
    _inherit = 'account.move'

    client_name = fields.Char(string="Client Name")
    client_mobile = fields.Char(string="Client Mobile Number")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    client_name = fields.Char(string="Client Name")
    client_mobile = fields.Char(string="Client Mobile Number")
    lpo_no = fields.Char(string="LPO No.")
    invoice_no = fields.Char(string="Invoice No.")
    add_address = fields.Text(string="Additional Delivery Address")
