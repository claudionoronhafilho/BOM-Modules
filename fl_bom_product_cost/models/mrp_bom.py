# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    bom_total_cost = fields.Float('Total BoM Cost', compute='_compute_bom_total_cost')

    @api.depends('bom_line_ids', 'bom_line_ids.product_qty', 'bom_line_ids.product_standard_price', 'product_qty')
    def _compute_bom_total_cost(self):
        for bom in self:
            cost = 0.0
            for line in bom.bom_line_ids:
                cost = cost + line.product_total_cost
            total_cost = cost / bom.product_qty
            bom.bom_total_cost = total_cost


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    product_standard_price = fields.Float('Cost', related='product_id.standard_price')
    product_total_cost = fields.Float('Total Cost', compute='_compute_total_cost')

    @api.depends('product_qty', 'product_standard_price')
    def _compute_total_cost(self):
        for record in self:
            record.product_total_cost = record.product_qty * record.product_standard_price
