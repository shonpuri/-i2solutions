
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

    tax_count = fields.Float(compute='_compute_tax_total')


    # @api.depends('tax_id','price_subtotal')
    # def _compute_tax_total(self):
    #     for tax in self:
    #         tax.tax_count = tax.tax_id * tax.price_subtotal

class AccountMove(models.Model):
    _inherit = 'account.move'

    client_name = fields.Char(string="Client Name")
    client_mobile = fields.Char(string="Client Mobile Number")

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    client_name = fields.Char(string="Client Name")
    client_mobile = fields.Char(string="Client Mobile Number")
