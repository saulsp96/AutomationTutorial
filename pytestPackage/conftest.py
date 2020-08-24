import pytest

@pytest.fixture()
def setUp():
    print("setUp: Running method level")
    yield
    print("tearDown: Running method level")

@pytest.fixture(scope="class")
def oneTimeSetUp(request,browser):
    print("oneTimeSetUp:Once before every module")
    if browser == 'firefox':
        value = 20
        print("Running test on FF")
    else:
        value = 10
        print("Running on: " + browser)
    if request.cls is not None:
        request.cls.value = value

    yield value
    print("oneTimeTearDown:Once after every module")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help='Type of operating system.')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")



