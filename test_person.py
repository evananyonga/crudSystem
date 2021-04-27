from models import Person


class TestModels:

    def test_can_retrieve_name(self):
        assert Person.name() == ""
