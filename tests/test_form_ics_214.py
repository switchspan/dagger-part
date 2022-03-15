import os

import pytest

from ics_forms import ICS214Form

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def valid_pdf():
    return os.path.join(THIS_DIR, 'test_ics_214.pdf')


@pytest.fixture()
def invalid_pdf():
    return os.path.join(THIS_DIR, 'invalid_file.pdf')


def test_loading_valid_form_returns_fema_author(valid_pdf):
    # print('Test file path = ', TEST_FILE_PATH)
    form = ICS214Form(valid_pdf)
    assert form.metadata["author"] == "FEMA"


def test_loading_valid_form_returns_mapped_fields(valid_pdf):
    form = ICS214Form(valid_pdf)
    assert form.incident_name == 'TEST INCIDENT'


def test_loading_valid_form_returns_mapped_resources(valid_pdf):
    form = ICS214Form(valid_pdf)
    assert form.number_of_resources_assigned() > 0
