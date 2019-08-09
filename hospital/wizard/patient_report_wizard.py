from odoo import api, fields, models


class Patient_Report_Wizard(models.TransientModel):
    _name = 'print.report'

    hospital_id = fields.Many2one('hospital.hospital', 'hospital')

    @api.multi
    def check_report(self):
        data = {}
        data["form"] = self.read(['hospital_id'])
        return self._print_report(data)
