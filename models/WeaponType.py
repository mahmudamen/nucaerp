from odoo import fields, models, api


class WeaponType(models.Model):
    _name = 'sec.weapontype'
    _description = 'نوع السلاح'

    id = fields.Integer('كود')
    name = fields.Char('اسم السلاح' , required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"