import os
import unittest

from pdfform import PdfForm

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_PATH = os.path.join(THIS_DIR, 'test_ics_213.pdf')
INVALID_FILE_PATH = os.path.join(THIS_DIR, 'invalid_file.pdf')


class TestPdfForm(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        form = PdfForm(TEST_FILE_PATH)
        # print("Meta data = ", form.metadata)
        # print("Form data =", form.data)
        self.assertEqual(form.metadata["author"], "FEMA")

    def test_loading_invalidform_raises_exception(self):
        with self.assertRaises(Exception):
            form = PdfForm(INVALID_FILE_PATH)

    def test_get_form_name_with_validform_returns_name(self):
        form = PdfForm(TEST_FILE_PATH)
        self.assertEqual(form.get_form_name(), "ICS Form 213, General Message")


if __name__ == '__main__':
    unittest.main()
