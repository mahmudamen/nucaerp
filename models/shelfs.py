from odoo import models, fields


class shelfs(models.Model):
    _name = 'sec.shelfs'
    _description = 'كود الرف'
    id = fields.Integer('كود ')
    name = fields.Char("كود الرف", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"