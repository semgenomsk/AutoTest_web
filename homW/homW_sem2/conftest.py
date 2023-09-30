import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_input_login():
    return """//span[text() = 'Username']/following::input[@type= 'text'][1]"""


@pytest.fixture()
def selector_input_password():
    return """//span[text() = 'Password']/following::input[@type= 'password'][1]"""


@pytest.fixture()
def selector_button():
    return """//button[@type= 'submit']"""


@pytest.fixture()
def selector_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def selector_blog():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def selector_create():
    return """//button[@id="create-btn"]"""


@pytest.fixture()
def selector_title_create():
    return """//span[text() = 'Title']/following::input[@type= 'text'][1]"""


@pytest.fixture()
def selector_description_create():
    return """//span[text() = 'Description']//following::textarea[1]"""


@pytest.fixture()
def selector_content_create():
    return """//span[text() = 'Content']//following::textarea[1]"""


@pytest.fixture()
def selector_title_public():
    return """//h1[@class ='svelte-tv8alb']"""


@pytest.fixture()
def selector_content_public():
    return """//div[@class = 'content svelte-tv8alb']"""


@pytest.fixture()
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close_dr()