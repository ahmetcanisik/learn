from validatev2 import is_valid_email


def test_is_valid_email():
    # These tests are expected "truthy"
    assert is_valid_email("imcanisik@gmail.com") == True
    assert is_valid_email("imcanisik@gmail.edu") == True
    assert is_valid_email("malan@cs50.harvard.edu") == True
    assert is_valid_email("ahmet@a.eduroam.edu") == True

    # These tests are expected "falsy"
    assert is_valid_email("@gmail.com") == False
    assert is_valid_email("gmail.com") == False
    assert is_valid_email("imcanisik@gmailcom") == False
    assert is_valid_email("imcanisik@gmail?com") == False
    assert is_valid_email("imcanisik@@@gmail.com") == False
