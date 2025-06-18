# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.release import version_info

class ResCompany(models.Model):
    _inherit = "res.company"

    nombre_comercial = fields.Char('Nombre Comercial')
    certificador_fel = fields.Selection([], 'Certificador FEL')
    afiliacion_iva_fel = fields.Selection([('GEN', 'GEN'), ('PEQ', 'PEQ'), ('EXE', 'EXE')], 'Afiliación IVA FEL', default='GEN')
    tipo_personeria_fel = fields.Char('Tipo Personeria FEL')
    frases_fel = fields.Text('Frases FEL')
    adenda_fel = fields.Text('Adenda FEL')

    # Restricción para validar que el nombre comercial esté definido
    @api.constrains('nombre_comercial', 'certificador_fel')
    def _check_nombre_comercial_fel(self):
        for rec in self:
            if rec.certificador_fel and not rec.nombre_comercial:
                raise ValidationError("Debe ingresar el campo 'Nombre Comercial' para emitir FEL con un certificador asignado.")