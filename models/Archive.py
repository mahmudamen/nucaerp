from odoo import fields, models, api


class Archive(models.Model):
    _name = 'sec.archive'
    _description = 'الارشيف الالكتروني'

    id = fields.Integer('كود')
    saveyear = fields.Char('عام الحفظ')
    parties = fields.Many2one('sec.parties', 'الجهة')
    cupboardnumber = fields.Integer('رقم الدولاب ')
    shelfnumber = fields.Integer('رقم الرف')
    filenumber = fields.Integer('رقم الملف')
    about = fields.Text('نبذه عن المكاتبة')
    notes = fields.Text('ملاحظات')
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"

