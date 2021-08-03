from odoo import fields, models, api


class Savelocation(models.Model):
    _name = 'sec.savelocation'
    _description = ' مكان الحفظ'
    id = fields.Integer('كود ')
    name = fields.Char("مكان الحفظ", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"
