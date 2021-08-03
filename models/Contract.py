from odoo import models, fields, api


class Contract(models.Model):
    _name = 'sec.contract'
    _description = 'كود التعاقدات '

    id = fields.Integer("كود")
    name = fields.Char("التعاقد", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"
