from odoo import models, fields, api


class PersonalData(models.Model):
    _name = 'sec.personaldata'
    _description = 'البيانات الشخصية '

    id = fields.Integer("كود")
    name = fields.Char("الاسم", required=True)
    birthdate = fields.Date("تاريخ الميلاد", required=True)
    nationalid = fields.Char("الرقم القومي", required=True)
    parties = fields.Many2one('sec.parties', 'الجهة')
    hiringdate = fields.Date('تاريخ التعيين')
    functionalclass = fields.Many2one('sec.functionalclass', 'الدرجة الوظيفية')
    job = fields.Many2one('sec.job', 'الوظيفة')
    qualification = fields.Char("المؤهل")
    socialstatus = fields.Many2one('sec.socialstatus', "الحالة الاجتماعية")
    transporter = fields.Many2one('sec.parties', 'الجهة')
    transporterdate = fields.Date('تاريخ النقل')
    transporterid = fields.Integer('رقم قرار النقل')
    confidentialreports = fields.Char('التقارير السرية')
    Sanctions = fields.Text('الجزاءات')
    address = fields.Char('العنوان')
    homephone = fields.Char('تليفون المنزل')
    mobile = fields.Char('الموبيل')
    notes = fields.Text('ملاحظات')
    image_1920 = fields.Binary(" ")
    approvalnu = fields.Integer('رقم الموافقة')
    approvaldate = fields.Date("تاريخ الموافقة")
    documents = fields.Binary("الموافقة الامنية")
    basicdata = fields.One2many('sec.basicdata', 'basicdata_id', string="  ")
    basicdatadetail = fields.One2many('sec.basicdatadetail',"basicdatadetail_id",string=" ")
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"


class Basicdata(models.Model):
    _name = 'sec.basicdata'
    _description = 'البيانات الاساسية '

    basicdata_id = fields.Many2one('sec.personaldata',"كود")
    fileno = fields.Integer("رقم الملف", required=True)
    followupstatus = fields.Many2one('sec.followup', 'حالة المتابعة')
    followupdate = fields.Date('تاريخ المتابعة')
    transporter = fields.One2many('sec.basicdatadetail', 'id', 'الجهة')


class Basicdatadetail(models.Model):
    _name = 'sec.basicdatadetail'
    _description = ' تفاصيل الجهات'

    basicdatadetail_id = fields.Many2one('sec.personaldata',"كود")
    transporter = fields.Many2one('sec.parties', 'الجهة')
    date = fields.Date('تاريخ')
    decision = fields.Integer('رقم القرار')
