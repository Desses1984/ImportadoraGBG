# -*- coding: utf-8 -*-

from odoo import fields, models 


class Plants(models.Model):
     _name = 'nursery.plant'
#     _description = 'plant_nursury.plant_nursury'

      name = fields.Char(string="Plant Name")
      price = fields.float()
        
        
        
        
class Customer(models.Model): 
     _name = 'nursery.customer'
      name = fields.Char(string="Customer Name", required=True)
      email = fields.Char(help="To Recieve the newsletter")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

