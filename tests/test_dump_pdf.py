import os
import unittest

# PDF form constants
from dump_pdf import extract_form_fields

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_PATH = os.path.join(THIS_DIR, 'test_ics_213.pdf')
INVALID_FILE_PATH = os.path.join(THIS_DIR, 'invalid_file.pdf')


class TestExtractFormFields(unittest.TestCase):
    def test_extract_form_fields_with_valid_form_returns_data(self):
        result = extract_form_fields(TEST_FILE_PATH)
        # print(result)
        self.assertTrue(result)  # assert we get a value back

    def test_extract_form_fields_with_invalid_form_returns_nothing(self):
        result = extract_form_fields(INVALID_FILE_PATH)
        # print(result)
        self.assertFalse(result)  # assert we get a value back


if __name__ == '__main__':
    unittest.main()
