# Copyright 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    @api.multi
    def update_price(self, virtual_room_id, date, price):
        vroom = self.env['hotel.room.type'].browse(virtual_room_id)
        pritem_obj = self.env['product.pricelist.item']
        for record in self:
            plitem = pritem_obj.search([
                ('pricelist_id', '=', record.id),
                ('product_tmpl_id', '=', vroom.product_id.product_tmpl_id.id),
                ('date_start', '=', date),
                ('date_end', '=', date),
                ('applied_on', '=', '1_product'),
                ('compute_price', '=', 'fixed')
            ])
            if plitem:
                plitem.fixed_price = price
            else:
                pritem_obj.create({
                    'pricelist_id': record.id,
                    'product_tmpl_id': vroom.product_id.product_tmpl_id.id,
                    'date_start': date,
                    'date_end': date,
                    'applied_on': '1_product',
                    'compute_price': 'fixed',
                    'fixed_price': price
                })
