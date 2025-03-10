import pytest
from selenium import webdriver

from config.pet_payloads import generate_random_pet
from api_clients.pet_client import PetClient


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver

    driver.quit()

@pytest.fixture
def created_pet():
    payload = generate_random_pet()
    response = PetClient.create_pet(payload)
    assert response.status_code == 200, "Failed to create a pet"

    pet_id = response.json().get("id")
    assert pet_id is not None, "Pet ID is missing in response"

    pet_id = response.json()["id"]

    yield pet_id

    delete_response = PetClient.delete_pet(pet_id)
    assert delete_response.status_code == 200