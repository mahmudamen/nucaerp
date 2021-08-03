from odoo import fields, models, api


class Job(models.Model):
    _name = 'sec.job'
    _description = 'كود الوظيفة'
    id = fields.Integer('كود ')
    name = fields.Char("كود الوظيفة", required=True)
    state = fields.Selection([('active','نشط'),('inactive','غير نشط')],string="state", defualt='active')

    def action_active(self):
        self.state = "active"

    def action_inactive(self):
        self.state = "inactive"