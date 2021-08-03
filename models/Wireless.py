from odoo import fields, models, api


class Wireless(models.Model):
    _name = 'sec.wireless'
    _description = 'الاجهزة اللاسلكية'

    id = fields.Integer('كود')
    parties = fields.Many2one('sec.parties', 'الجهة')
    brand = fields.Char('ماركة الجهاز')
    devicestatus = fields.Char('حالة الجهاز')
    devicenumber = fields.Integer('العدد')
    deviceserial = fields.Char('رقم الجهاز')
    deviceuser = fields.Char('مستخدم الجهاز')
    letternumber = fields.Char('رقم الخطاب')
    letterdate = fields.Date('تاريخ الخطاب')
    notes = fields.Text('ملاحظات')
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"