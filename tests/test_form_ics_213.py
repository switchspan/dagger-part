import unittest

from ics_forms import ICS213Form


class TestFormIcs213(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        form = ICS213Form('test_ics_213.pdf')
        # print(form)
        # print("Meta data = ", form.metadata)
        # print("Form data =", form.data)
        self.assertEqual(form.metadata["author"], "FEMA")

    def test_loading_validform_returns_mapped_fields(self):
        form = ICS213Form('test_ics_213.pdf')
        self.assertEqual(form.subject, 'TEST MESSAGE')


if __name__ == '__main__':
    unittest.main()
