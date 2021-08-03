from odoo import fields, models, api


class Followup(models.Model):
    _name = 'sec.followup'
    _description = 'كود المتابعة'
    id = fields.Integer('كود')
    name = fields.Char("كود المتابعة", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"