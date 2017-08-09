from odoo import http
from odoo.http import request
from odoo import models, fields, api
import json

class Products(http.Controller):
    @http.route(['/page/website.products_clearance', '/page/products_clearance'], type='http', auth="public", website=True)
    def index(self, **kw):


        Products = http.request.env['product.product']

        var_products = Products.search([])

        return http.request.render('thanos_productos_liquidacion.index', {
            'products_clearance': var_products
        })
