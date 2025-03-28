# -*- coding: utf-8 -*-

from odoo import models, fields

class Electrodomestico(models.Model):
    _name = 'electrodomestico'
    _description = 'Electrodoméstico'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código de Producto', required=True)
    pais_id = fields.Many2one('res.country', string='País', required=True)
    importe_compra = fields.Float(string='Importe de Compra')
    moneda_id = fields.Many2one('res.currency', string='Moneda', required=True)
    precio_venta = fields.Float(string='Precio de Venta')