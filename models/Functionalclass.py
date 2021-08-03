from odoo import fields, models, api


class Functionalclass(models.Model):
    _name = 'sec.functionalclass'
    _description = 'كود الدرجة الوظيفية'
    id = fields.Integer('كود ')
    name = fields.Char('الدرجة الوظيفية', required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"