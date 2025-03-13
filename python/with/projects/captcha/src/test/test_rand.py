from rand import rand

def test_length():
    assert len(rand(0)) == 0

def test_numbers():
    assert int(rand(1, numbers=True)) >= 0
    
def test_chars():
    assert rand(1, chars=True) != ""

def test_turkish_chars():
    assert rand(2, turkishChars=True) != "s"

def test_special_chars():
    assert rand(3, numbers=False, specialChars="-") == "---"
    
