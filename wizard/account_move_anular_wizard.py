# -*- encoding: utf-8 -*-

from odoo import fields, models, _
from odoo.exceptions import UserError


class AccountMoveAnularWizard(models.TransientModel):
    _name = 'account.move.anular.wizard'
    _description = 'Anular factura'

    move_id = fields.Many2one('account.move', string='Factura', required=True, readonly=True)
    motivo_fel = fields.Char(string='Motivo de anulación', required=True)

    def action_confirm(self):
        self.ensure_one()
        if self.move_id.state != 'posted':
            raise UserError(_('Solo se pueden anular facturas publicadas.'))
        self.move_id.motivo_fel = self.motivo_fel
        return self.move_id.action_anular_factura()
