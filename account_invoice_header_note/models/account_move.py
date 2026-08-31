from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    header_note = fields.Html(
        string='Header Note',
        help='Free text shown above the invoice lines, both in the form view '
        'and on the printed invoice. The counterpart of the Terms and '
        'Conditions printed below the lines.',
    )
