import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed")
    yield
    print(" I will executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Vamsi", "Krishna", "vamsikowluri934.com"]


@pytest.fixture(params= [("Microsoft Edge","Vamsi"), "Firefox", "google chrome"])
def crossBrowser(request):
    return request.param
