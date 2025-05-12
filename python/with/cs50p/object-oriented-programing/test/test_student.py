from student import get_student


def test_get_student():
    student = get_student("Harry", "Gryffindor", "Expecto Patronum")
    assert str(student) == "Harry from Gryffindor"

    student.house = "Number four, Privet Drive"
    assert str(student) == "Harry from Number four, Privet Drive"
