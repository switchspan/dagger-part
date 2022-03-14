import unittest

from pdfrw import PdfReader


class PdfForm:
    """Loads and manages PDF forms"""

    def __init__(self, pdf_file_path):
        """Constructor for PdfForm"""
        self.pdf_file_path = pdf_file_path
        file_data = PdfReader(pdf_file_path)
        if isinstance(file_data.Info["/Author"], type(None)):
            raise Exception("Invalid PDF form file!")
        self.author = file_data.Info["/Author"][1:-1]
        self.form_name = file_data.Info["/Title"][1:-1]
        self.data = file_data


class TestPdfForm(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        form = PdfForm('test_ics_213.pdf')
        self.assertEqual(form.author, "FEMA")  # add assertion here

    def test_loading_invalidform_raises_exception(self):
        with self.assertRaises(Exception):
            form = PdfForm('invalid_file.pdf')


if __name__ == '__main__':
    unittest.main()
