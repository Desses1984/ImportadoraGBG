# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductDetail(models.Model):
    _name = 'product.detail'

    logo = fields.Binary(string="Icono", readonly=False)

    name = fields.Char(
        string='Name',
    )

    code = fields.Char(
        string='Code',
    )
