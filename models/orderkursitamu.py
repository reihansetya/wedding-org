from odoo import api, fields, models


class OrderKursiTamu(models.Model):
    _name = 'wedding.orderkursitamu'
    _description = 'New Description'

    name = fields.Char(string='Kode Order')


class OrderKursiTamuDetail(models.Model):
    _name = 'wedding.orderkursitamudetail'
    _description = 'New Description'

    name = fields.Char(string='Name')
