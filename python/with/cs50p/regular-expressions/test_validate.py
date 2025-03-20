import pytest
from validate import is_valid_email

def test_is_valid_email():
    assert is_valid_email("imcanisik@gmail.com") == True
    assert is_valid_email("gmail.com") == False