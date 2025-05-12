from names import hello


def test_default_argument():
    assert hello() == "Hello, world"


def test_arguments():
    assert hello("Ahmet") == "Hello, Ahmet"
