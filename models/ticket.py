from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ITTicket(models.Model):
    _name = 'it.ticket'
    _description = 'Ticket d\'intervention'

    name = fields.Char(string='Titre', required=True)
    description = fields.Text(string='Description du problème')
    equipment_id = fields.Many2one('it.equipment', string='Équipement concerné', required=True)
    state = fields.Selection([
        ('new', 'Nouveau'),
        ('in_progress', 'En cours'),
        ('resolved', 'Résolu'),
    ], string='Statut', default='new', required=True)
    date_created = fields.Datetime(string='Date de création', default=fields.Datetime.now)
    
    technician_id = fields.Many2one('hr.employee', string='Technicien assigné')
    
    def action_start(self):
        self.state = 'in_progress'

    def action_resolve(self):
        self.state = 'resolved'
        
    @api.constrains('equipment_id')
    def _check_equipment_active(self):
        for record in self:
            if not record.equipment_id.is_active:
                raise ValidationError("Impossible de créer un ticket sur un équipement hors service.")
