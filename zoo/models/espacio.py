# -*- coding: utf-8 -*-

from odoo import models, fields, api


class zoo(models.Model):
    _name = 'zoo.espacio'
    _description = 'Espacio del Zoológico'

    id_espacio = fields.Char(string='Id de Espacio', required=True)
    tipo = fields.Selection([
        ('jaula', 'Jaula'),
        ('vallado', 'Vallado'),
        ('acuario', 'Acuario'),
        ('terrarium', 'Terrarium'),
    ], string='Tipo de Espacio', required=True)
    
    area_tematica = fields.Selection([
        ('europa', 'Europa'),
        ('asia', 'Asia'),
        ('africa', 'África'),
        ('america', 'América'),
        ('oceania', 'Oceanía'),
    ], string='Área Temática')
