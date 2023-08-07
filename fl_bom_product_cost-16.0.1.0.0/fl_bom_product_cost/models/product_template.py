# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_bom_cost = fields.Float('Total BoM Cost', compute='_compute_product_bom_cost')

    def _compute_product_bom_cost(self):
        for product in self:
            total_cost = 0.0
            boms = self.env['mrp.bom'].search([('product_tmpl_id', '=', product.id)])
            for bom in boms:
                total_cost = total_cost + bom.bom_total_cost
            product.product_bom_cost = total_cost


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_bom_cost = fields.Float('Total BoM Cost', compute='_compute_product_bom_cost')

    def _compute_product_bom_cost(self):
        for product in self:
            total_cost = 0.0
            boms = self.env['mrp.bom'].search(['|', ('product_id', '=', product.id), '&', ('product_id', '=', False), ('product_tmpl_id', '=', product.product_tmpl_id.id)])
            for bom in boms:
                total_cost = total_cost + bom.bom_total_cost
            product.product_bom_cost = total_cost