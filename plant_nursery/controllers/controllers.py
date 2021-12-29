# -*- coding: utf-8 -*-
# from odoo import http


# class DeExample(http.Controller):
#     @http.route('/de_example/de_example', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_example/de_example/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_example.listing', {
#             'root': '/de_example/de_example',
#             'objects': http.request.env['de_example.de_example'].search([]),
#         })

#     @http.route('/de_example/de_example/objects/<model("de_example.de_example"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_example.object', {
#             'object': obj
#         })
