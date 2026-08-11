from odoo import models, fields, api

class ITEquipment(models.Model):
    _name = 'it.equipment'
    _description = 'Équipement Informatique'

    name = fields.Char(string='Nom', required=True)
    equipment_type = fields.Selection([
        ('laptop', 'Ordinateur portable'),
        ('desktop', 'Ordinateur fixe'),
        ('printer', 'Imprimante'),
        ('phone', 'Téléphone'),
    ], string='Type', required=True)
    serial_number = fields.Char(string='Numéro de série')
    purchase_date = fields.Date(string='Date d\'achat')
    is_active = fields.Boolean(string='En service', default=True)
    ticket_ids = fields.One2many('it.ticket', 'equipment_id', string='Tickets')
    ticket_count = fields.Integer(string='Nombre de tickets', compute='_compute_ticket_count')

    @api.depends('ticket_ids')
    def _compute_ticket_count(self):
        for record in self:
            record.ticket_count = len(record.ticket_ids)
            
    def action_view_tickets(self):
        self.ensure_one()
        return {
            'name': 'Tickets',
            'type': 'ir.actions.act_window',
            'res_model': 'it.ticket',
            'view_mode': 'tree,form',
            'domain': [('equipment_id', '=', self.id)],
        }
