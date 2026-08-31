# Account Invoice Header Note

Rich text note shown and printed **above** the invoice lines table.

Odoo prints the *Terms and Conditions* (`narration`) below the invoice lines.
This module adds the missing counterpart above them: a `header_note` HTML field
on `account.move`, rendered in the *Invoice Lines* tab directly above the lines
and inserted into the invoice PDF right before the lines table.

## Installation

The module lives in this repository's `addons/` directory, which is already on
the Odoo addons path. Update the apps list and install
`account_invoice_header_note`.

## Usage

Open an invoice, type into the note area above the lines, print. See
`readme/USAGE.md` for details.

## Configuration

None. The field is free text per invoice — there is no company-level default,
by design.

## Technical notes

| Item | Value |
| --- | --- |
| Model | `account.move` |
| Field | `header_note` (`fields.Html`) |
| Form anchor | `account.view_move_form`, before `invoice_line_ids` in `page[@id='invoice_tab']` |
| Report anchor | `account.report_invoice_document`, before `table[@name='invoice_line_table']` |

Related work that solves a *different* problem: OCA's `base_comment_template` /
`account_comment_template` place predefined, reusable comment blocks before or
after the lines. Use those when the text is a template chosen from a list; use
this module when it is typed per invoice.

## Credits

- Maik Derstappen \<md@derico.de\>

## License

AGPL-3
