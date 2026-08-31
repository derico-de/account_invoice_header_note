{
    'name': 'Account Invoice Header Note',
    'summary': 'Rich text note shown and printed above the invoice lines table',
    'version': '19.0.1.0.0',
    'development_status': 'Beta',
    'category': 'Accounting/Accounting',
    'author': 'derico',
    'website': 'https://derico.de',
    'support': 'md@derico.de',
    'license': 'AGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'views/account_move_views.xml',
        'views/report_invoice.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
