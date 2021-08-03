from odoo import fields, models, api


class Contractsdata(models.Model):
    _name = 'sec.contractsdata'
    _description = 'بيانات التعاقدات'

    id = fields.Integer("كود")
    parties = fields.Many2one('sec.parties', 'الجهة')
    approvaldate = fields.Date('تاريخ الموافقة')
    offernotenumber = fields.Integer('رقم مذكرة العرض')
    datestartguard = fields.Date('تاريخ بداية الخفرة')
    dateendguard = fields.Date('تاريخ نهاية الخفرة')
    typecontract = fields.Many2one('sec.typecontact', 'نوع التعاقد')
    contracts = fields.Many2one('sec.contract','موقف التعاقد')
    guardnumber = fields.Integer('عدد افراد الخفرة')
    monthlyvalue = fields.Float('القيمة الشهرية')
    annualvalue = fields.Float('القيمة السنوية' , compute='_computeVar')
    guardplace = fields.Text('مكان الخفرة')
    notes = fields.Text('ملاحظات')
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"

    @api.depends('monthlyvalue')
    def _computeVar(self):
        for record in self:
            record.annualvalue = record.monthlyvalue * 12
