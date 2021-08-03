from odoo import fields, models, api


class ModelName(models.TransientModel):
    _name = 'sec.TableName'
    _description = 'Description'

    name = fields.Char()
