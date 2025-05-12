from sleep import sheep
def test_sheep():
    assert sheep(0) == ""
    assert sheep(1) == "🐑"
    assert sheep(2) == "🐑🐑"