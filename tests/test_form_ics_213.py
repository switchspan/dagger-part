import unittest

from pdfform import PdfForm


class FormIcs213(PdfForm):
    FIELD_MAPPING = {
        "1 Incident Name Optional": "incident_name",
        "2 To Name and Position": "to_name",
        "3 From Name and Position": "from_name",
        "4 Subject": "subject",
        "5 Date": "date",
        "6 Time": "time",
        "7 Message": "message_text",
        "8 Approved by Name": "approved_by_name",
        "Signature_19": "",
        "PositionTitle_13": "approved_by_position",
        "9 Reply": "reply_text",
        "10 Replied by Name": "replied_by_name",
        "PositionTitle_14": "replied_by_position",
        "Signature_20": "",
        "DateTime_14": "date_time"
    }

    incident_name = ''
    to_name = ''
    from_name = ''
    subject = ''
    date = ''
    time = ''
    message_text = ''
    approved_by_name = ''
    approved_by_position = ''
    reply_text = ''
    replied_by_name = ''
    replied_by_position = ''
    date_time = ''

    def __init__(self, pdf_file_path):
        super().__init__(pdf_file_path)


class TestFormIcs213(unittest.TestCase):
    def test_loading_validform_returns_FEMA_author(self):
        form = FormIcs213('test_ics_213.pdf')
        # print(form)
        # print("Meta data = ", form.metadata)
        # print("Form data =", form.data)
        self.assertEqual(form.metadata["author"], "FEMA")

    def test_loading_validform_returns_mapped_fields(self):
        form = FormIcs213('test_ics_213.pdf')
        self.assertEqual(form.subject, 'TEST MESSAGE')


if __name__ == '__main__':
    unittest.main()
