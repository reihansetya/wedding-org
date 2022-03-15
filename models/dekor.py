from odoo import api, fields, models


class Dekor(models.Model):
    _name = 'wedding.dekor'
    _description = 'Model untuk tabel dekor'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga Dekorasi')
    deskripsi = fields.Char(string='Deskripsi Dekorasi')
