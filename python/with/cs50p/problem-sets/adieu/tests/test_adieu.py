from adieu import Adieu

def test_adieu():
    names = ["Ahmet", "Mehmet", "Halil"]
    adieu = Adieu()

    assert adieu.say(names[0]) == f"{adieu.prefix}Ahmet"
    assert adieu.say(*names[:2]) == f"{adieu.prefix}Ahmet and Mehmet"
    assert adieu.say(*names) == f"{adieu.prefix}Ahmet, Mehmet and Halil"