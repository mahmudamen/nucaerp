from odoo import fields, models, api


class Functionalclass(models.Model):
    _name = 'sec.functionalclass'
    _description = 'كود الدرجة الوظيفية'
    id = fields.Integer('كود ')
    name = fields.Char('الدرجة الوظيفية', required=True)
    personal_count = fields.Integer(compute='compute_count')

    def compute_count(self):
        for record in self:
            record.personal_count = self.env['sec.personaldata'].search_count(
                [('functionalclass', '=', self.id)])

    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"

    def get_person(self):
        return {
            'name': ('personal'),
            'domain':[('functionalclass','=',self.id)],
            'view_type':'form',
            'res_model':'sec.personaldata',
            'view_id':False,
            'view_mode':'tree,form',
            'type':'ir.actions.act_window',

        }