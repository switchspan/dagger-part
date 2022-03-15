import unittest

from pdfform import PdfForm


class TestPdfForm(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        form = PdfForm('test_ics_213.pdf')
        # print("Meta data = ", form.metadata)
        # print("Form data =", form.data)
        self.assertEqual(form.metadata["author"], "FEMA")

    def test_loading_invalidform_raises_exception(self):
        with self.assertRaises(Exception):
            form = PdfForm('invalid_file.pdf')

    def test_get_form_name_with_validform_returns_name(self):
        form = PdfForm('test_ics_213.pdf')
        self.assertEqual(form.get_form_name(), "ICS Form 213, General Message")


if __name__ == '__main__':
    unittest.main()
