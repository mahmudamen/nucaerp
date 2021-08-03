from odoo import models, fields


class Socialstatus(models.Model):
    _name = 'sec.socialstatus'
    _description = 'كود الحالة الاجتماعية'
    id = fields.Integer('كود ')
    name = fields.Char("الحالة الاجتماعية", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"