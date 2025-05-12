from big_number import bign


def test_bign():
    assert bign(0) == "0.00"
    assert bign(1) == "1.00"
    assert bign(10) == "10.00"
    assert bign(100) == "100.00"
    assert bign(1000) == "a thousand"
    assert bign(10000) == "10k"
    assert bign(100000) == "100k"
    assert bign(1000000) == "a million"
    assert bign(10000000) == "10m"
    assert bign(100000000) == "100m"
    assert bign(1000000000) == "a billion"
