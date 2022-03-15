import os.path

import pytest

from ics_forms import ICS213Form


@pytest.fixture()
def valid_pdf():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, 'test_ics_213.pdf')


def test_loading_valid_pdf_returns_fema_author(valid_pdf):
    # print('Test file path = ', valid_pdf)
    form = ICS213Form(valid_pdf)
    # print(form)
    # print("Meta data = ", form.metadata)
    # print("Form data =", form.data)
    assert form.metadata["author"] == "FEMA"


def test_loading_valid_pdf_returns_mapped_fields(valid_pdf):
    form = ICS213Form(valid_pdf)
    assert form.subject == 'TEST MESSAGE'
