{
    'name': 'Gestion de Parc Informatique',
    'version': '1.0',
    'summary': 'Gestion des équipements et tickets d\'intervention',
    'description': 'Module de gestion de parc IT avec suivi des interventions techniques.',
    'author': 'Nour El Imène',
    'category': 'Services',
    'depends': ['base', 'hr'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/equipment_views.xml',
        'views/ticket_views.xml',
        'reports/ticket_report.xml',
    ],
    'installable': True,
    'application': True,
}
