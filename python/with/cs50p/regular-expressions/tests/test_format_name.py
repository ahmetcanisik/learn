from format import format_name


def test_format_name():
    assert format_name("David Malan") == "David Malan"
    assert format_name("Malan, David") == "David, Malan"
