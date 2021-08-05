from odoo import fields, models, api


class TestWizard(models.TransientModel):
    _name = 'sec.testwizard'
    _description = 'Test Wizard'

    person_id = fields.Many2one('sec.personaldata',string='الموظف')
    date = fields.Date('التاريخ')

