# -*- coding: utf-8 -*-

from odoo import models, fields

class Cliente(models.Model):
    _name = 'cliente'
    _description = 'Cliente'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    nif = fields.Char(string='NIF')
    direccion = fields.Char(string='Dirección')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    telefono = fields.Char(string='Teléfono')
