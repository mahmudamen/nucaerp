from odoo import fields, models, api


class Typecontact(models.Model):
    _name = 'sec.typecontact'
    _description = '  نوع التعاقد'
    id = fields.Integer('كود ')
    name = fields.Char(" نوع التعاقد", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"
