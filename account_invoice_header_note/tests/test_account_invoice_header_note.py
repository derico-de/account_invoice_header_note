from lxml import etree
from odoo.addons.account.tests.common import AccountTestInvoicingCommon
from odoo.tests import tagged

NOTE_TEXT = 'Delivery according to order ORD-42'


@tagged('post_install', '-at_install')
class TestAccountInvoiceHeaderNote(AccountTestInvoicingCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.invoice = cls._create_invoice_one_line(
            partner_id=cls.partner_a,
            name='Consulting',
            price_unit=100.0,
        )

    def _render_invoice(self, invoice):
        html, _report_type = self.env['ir.actions.report']._render_qweb_html('account.report_invoice', invoice.ids)
        return html.decode()

    def test_header_note_empty_by_default(self):
        self.assertFalse(self.invoice.header_note)

    def test_header_note_field_precedes_lines_in_form(self):
        arch = self.env['account.move'].get_view(self.env.ref('account.view_move_form').id, 'form')['arch']
        page = etree.fromstring(arch).xpath("//page[@id='invoice_tab']")[0]
        # A union expression returns the nodes in document order, so this
        # asserts the note really is rendered above the lines.
        fields = page.xpath(".//field[@name='header_note'] | .//field[@name='invoice_line_ids']")
        self.assertEqual([f.get('name') for f in fields], ['header_note', 'invoice_line_ids'])

    def test_header_note_printed_above_lines(self):
        self.invoice.header_note = f'<p>{NOTE_TEXT}</p>'
        html = self._render_invoice(self.invoice)
        self.assertIn(NOTE_TEXT, html)
        self.assertLess(html.index(NOTE_TEXT), html.index('invoice_line_table'))

    def test_empty_header_note_not_printed(self):
        html = self._render_invoice(self.invoice)
        self.assertNotIn('name="header_note"', html)

    def test_header_note_kept_on_copy(self):
        self.invoice.header_note = f'<p>{NOTE_TEXT}</p>'
        self.assertIn(NOTE_TEXT, self.invoice.copy().header_note)
