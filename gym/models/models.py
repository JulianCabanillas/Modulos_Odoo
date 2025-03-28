from odoo import models, fields, api
class Classes(models.Model):
    
    _name = 'gym.classes'
    _description = 'Gym Classes'
    
    name = fields.Char(string="Title", required=True, help="Gym Zero Haker")
    description = fields.Text()
    start = fields.Datetime('Starts',required=True, default=fields.Datetime.now)
    end = fields.Datetime('Ends',required=True, default=fields.Datetime.now)
    capacity = fields.Integer("Capacity")
    activityType = fields.Selection([('dance','Dance'),
                                    ('aerobic','Aerobic'),
                                    ('anaerobic','Anaerobic'),
                                    ('relax','Relax'),],
                                    'Type of activity')
