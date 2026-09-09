# -*- encoding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    fel_annulment_journal_id = fields.Many2one(
        related='company_id.fel_annulment_journal_id',
        readonly=False,
    )
