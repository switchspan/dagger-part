import os

import pytest

from ics_forms import ICS214Form


@pytest.fixture()
def validpdf():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, 'test_ics_214.pdf')


@pytest.fixture()
def invalidpdf():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(this_dir, 'invalid_file.pdf')


def test_loading_validform_returns_FEMA_author(validpdf):
    # print('Test file path = ', TEST_FILE_PATH)
    form = ICS214Form(validpdf)
    assert form.metadata["author"] == "FEMA"


def test_loading_validform_returns_mapped_fields(validpdf):
    form = ICS214Form(validpdf)
    assert form.incident_name == 'TEST INCIDENT'


def test_loading_validform_returns_mapped_resources(validpdf):
    form = ICS214Form(validpdf)
    assert form.number_of_resources_assigned() > 0
