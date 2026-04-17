# -*- coding: utf-8 -*-
from odoo import api, models

class ReportAccountReport_Invoice(models.AbstractModel):
    _inherit = 'report.account.report_invoice'

    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        for invoice in docs:
            if not invoice.firma_fel:
                invoice.contingencia_fel = True
            else:
                invoice.contingencia_fel = False
        return super()._get_report_values(docids, data)