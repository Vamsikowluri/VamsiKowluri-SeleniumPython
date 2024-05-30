import pytest


@pytest.mark.usefixtures("setup")
class TextExample:
    def test_fixturedemo(self):
        print("I will execute steps in fixtureDemo method")
    def test_fixturedemo(self):
        print("I will execute steps in fixtureDemo1 method")
    def test_fixturedemo(self):
        print("I will execute steps in fixtureDemo2 method")
    def test_fixturedemo(self):
        print("I will execute steps in fixtureDemo3 method")



