# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Plants(models.Model):
     _name = 'nursury.plant'
#     _description = 'plant_nursury.plant_nursury'

      name = fields.Char("Plant Name")
      price = fields.float()
        
        
        
        
class Customer(models.Model): 
     _name = 'nursury.customer'
      name = fields.Char("Customer Name")
      email = fields.Char(help="To Recieve the newsletter")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
