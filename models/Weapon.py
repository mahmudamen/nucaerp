from odoo import fields, models, api


class Weapon(models.Model):
    _name = 'sec.weapon'
    _description = 'بيانات السلاح'

    id = fields.Integer('كود')
    parties = fields.Many2one('sec.parties', 'الجهة')
    weapontype = fields.Many2one('sec.weapontype','نوع السلاح')
    number = fields.Integer('العدد')
    weaponnumber = fields.Char('رقم السلاح')
    weaponstate = fields.Selection(selection=[('1', 'صالح'),('2', 'غير صالح')] ,string='حالة السلاح' , default='1')
    weaponuser = fields.Char('مستخدم السلاح')
    weaponplace = fields.Selection(selection=[('1', 'مبني الجهاز'), ('2', 'قسم الشرطة ')], string='مكان السلاح', default='1')
    ammo = fields.Selection(selection=[('1', '9 مم'), ('2', 'خرطوش ')], string='الذخيرة', default='1')
    ammonumber = fields.Integer('عدد الذخيرة')
    notes = fields.Text('ملاحظات')
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"
