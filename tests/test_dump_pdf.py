import unittest

# PDF form constants
from dump_pdf import extract_form_fields


class TestExtractFormFields(unittest.TestCase):
    def test_extract_form_fields_with_valid_form_returns_data(self):
        result = extract_form_fields('test_ics_213.pdf')
        # print(result)
        self.assertTrue(result)  # assert we get a value back

    def test_extract_form_fields_with_invalid_form_returns_nothing(self):
        result = extract_form_fields('invalid_file.pdf')
        # print(result)
        self.assertFalse(result)  # assert we get a value back


if __name__ == '__main__':
    unittest.main()
