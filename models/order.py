from base64 import encode
from odoo import api, fields, models


class Order(models.Model):
    _name = 'wedding.order'
    _description = 'New Description'

    name = fields.Char(string='Kode Order', required=True)

    orderdetail_ids = fields.One2many(
        comodel_name='wedding.order_detail',
        inverse_name='order_id',
        string='Order Detail')

    tanggal_pesan = fields.Datetime(
        'Tanggal Pemesanan',
        default=fields.Datetime.now())

    total = fields.Integer(
        compute="_compute_total",
        string='Total Harga',
        store=True)

    @api.depends('orderdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['wedding.order_detail'].search(
                [('order_id', '=', record.id)]).mapped('harga'))
            record.total = a


class OrderDetail(models.Model):
    _name = 'wedding.order_detail'
    _description = 'New Description'

    order_id = fields.Many2one(
        comodel_name='wedding.order',
        string='Order')
    panggung_id = fields.Many2one(
        comodel_name='wedding.panggung',
        string='Panggung')

    name = fields.Selection(
        string='Name',
        selection=[
            ('panggung', 'Panggung'),
            ('kursi tamu', 'Kursi Tamu'), ])
    harga = fields.Integer(
        compute='_compute_harga',
        string='harga',
        store=True)
    qty = fields.Integer(string='QTY')
    harga_satuan = fields.Integer(
        compute='_compute_harga_satuan', string='Harga Satuan')

    @api.depends('panggung_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.panggung_id.harga

    @api.depends('qty', 'panggung_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self, vals):
        record = super(OrderDetail, self).create(vals)
        if record.qty:
            self.env['wedding.panggung'].search(
                [('id', '=', record.panggung_id.id)]).write({'stok': record.panggung_id.stok-record.qty})
            return record
