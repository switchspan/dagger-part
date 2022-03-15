import os.path
import unittest

from ics_forms import ICS213Form

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_PATH = os.path.join(THIS_DIR, 'test_ics_213.pdf')


class TestFormIcs213(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        print('Test file path = ', TEST_FILE_PATH)
        form = ICS213Form(TEST_FILE_PATH)
        # print(form)
        # print("Meta data = ", form.metadata)
        # print("Form data =", form.data)
        self.assertEqual(form.metadata["author"], "FEMA")

    def test_loading_validform_returns_mapped_fields(self):
        form = ICS213Form(TEST_FILE_PATH)
        self.assertEqual(form.subject, 'TEST MESSAGE')


if __name__ == '__main__':
    unittest.main()
