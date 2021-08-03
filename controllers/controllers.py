# -*- coding: utf-8 -*-
# from odoo import http


# class Nucaerp(http.Controller):
#     @http.route('/nucaerp/nucaerp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nucaerp/nucaerp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nucaerp.listing', {
#             'root': '/nucaerp/nucaerp',
#             'objects': http.request.env['nucaerp.nucaerp'].search([]),
#         })

#     @http.route('/nucaerp/nucaerp/objects/<model("nucaerp.nucaerp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nucaerp.object', {
#             'object': obj
#         })
