import os

import pytest

from pdfform import PdfForm

this_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def valid_pdf():
    return os.path.join(this_dir, 'test_ics_213.pdf')


@pytest.fixture()
def invalid_pdf():
    return os.path.join(this_dir, 'invalid_file.pdf')


def test_loading_valid_form_returns_fema_author(valid_pdf):
    form = PdfForm(valid_pdf)
    # print("Meta data = ", form.metadata)
    # print("Form data =", form.data)
    assert form.metadata["author"] == "FEMA"


def test_loading_invalid_form_raises_exception(invalid_pdf):
    with pytest.raises(Exception) as pdferror:
        form = PdfForm(invalid_pdf)
    assert pdferror.type is Exception


def test_get_form_name_with_valid_form_returns_name(valid_pdf):
    form = PdfForm(valid_pdf)
    assert form.get_form_name() == "ICS Form 213, General Message"
