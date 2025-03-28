# -*- coding: utf-8 -*-

from odoo import models, fields, api


class animal(models.Model):
    _name = 'animal'
    _description = 'Animal'

    nombre = fields.Char(string='Nombre', required=True)
    especie = fields.Char(string='Especie')
    id_animal = fields.Char(string='Id Animal', required=True)
    id_pais = fields.Many2one('res.country', string='País Procedencia Animal')
    edad = fields.Integer(string='Edad')
    fecha_entrada = fields.Date(string='Fecha de Entrada')

     

