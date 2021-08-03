from odoo import models, fields, api


class Lectures(models.Model):
    _name = 'sec.lectures'
    _description = 'المحاضرات '

    id = fields.Integer("كود")
    filename = fields.Char("اسم الملف")
    subject = fields.Char("الموضوع")
    showDate = fields.Date("تاريخ العرض", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"