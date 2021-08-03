from odoo import models, fields


class wheel(models.Model):
    _name = 'sec.wheel'
    _description = 'كود الدولاب'
    id = fields.Integer('كود ')
    name = fields.Char("كود الدولاب", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"