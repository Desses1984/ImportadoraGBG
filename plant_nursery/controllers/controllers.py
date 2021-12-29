# -*- coding: utf-8 -*-
# from odoo import http


# class PlantNursury(http.Controller):
#     @http.route('/plant_nursury/plant_nursury', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plant_nursury/plant_nursury/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('plant_nursury.listing', {
#             'root': '/plant_nursury/plant_nursury',
#             'objects': http.request.env['plant_nursury.plant_nursury'].search([]),
#         })

#     @http.route('/plant_nursury/plant_nursury/objects/<model("plant_nursury.plant_nursury"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plant_nursury.object', {
#             'object': obj
#         })
