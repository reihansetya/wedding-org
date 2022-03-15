from odoo import api, fields, models


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'

    name = fields.Char(string='Kode Order', required=True)

    orderdetail_ids = fields.One2many(
        comodel_name='wedding.order_detail', inverse_name='order_id', string='Order Detail')


class OrderDetail(models.Model):
    _name = 'wedding.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='wedding.order', string='Order')
    panggung_id = fields.Many2one(
        comodel_name='wedding.panggung', string='Panggung')

    name = fields.Selection(string='Name', selection=[(
        'panggung', 'Panggung'), ('kursi tamu', 'Kursi Tamu'), ])
