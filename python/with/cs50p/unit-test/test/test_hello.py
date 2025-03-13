from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_arguments():
    assert hello(2) == "Hello, 2"