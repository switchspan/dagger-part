import os

import pytest

# PDF form constants
from dump_pdf import extract_form_fields

this_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture()
def valid_pdf():
    return os.path.join(this_dir, 'test_ics_213.pdf')


@pytest.fixture()
def invalid_pdf():
    return os.path.join(this_dir, 'invalid_file.pdf')


def test_extract_form_fields_with_valid_form_returns_data(valid_pdf):
    result = extract_form_fields(valid_pdf)
    # print(result)
    assert len(result) > 0  # assert we get a value back


def test_extract_form_fields_with_invalid_form_returns_nothing(invalid_pdf):
    result = extract_form_fields(invalid_pdf)
    # print(result)
    assert result == {}  # assert we do NOT get a value back
