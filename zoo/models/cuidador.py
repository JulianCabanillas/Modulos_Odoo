# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cuidador(models.Model):
    _name = 'cuidador'
    _description = 'Cuidador'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos')
    cargo = fields.Selection([
        ('supervisor', 'Supervisor'),
        ('encargado', 'Encargado'),
        ('cuidador', 'Cuidador'),
    ], string='Cargo', required=True)
    fecha_incorporacion = fields.Date(string='Fecha de Incorporacion')

