import pytest

@pytest.fixture(scope="class")

def get_user():
    print("*** fixture ***")

def test(get_user):
    pass
