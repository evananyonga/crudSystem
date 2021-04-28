from models import Person


def test_is_full_name():
    full_name = Person()
    assert full_name.name()
