Odoo prints the *Terms and Conditions* (`narration`) **below** the invoice
lines. There is no counterpart above them, so any introductory text — a
greeting, a delivery reference, a project or contract number — has to be
squeezed into the first invoice line or into the customer address block.

This module adds a rich text field **Header Note** (`header_note`) to
`account.move`. It behaves like `narration`, but is shown above the invoice
lines in the backend form and printed above the invoice lines table on the
invoice PDF.
