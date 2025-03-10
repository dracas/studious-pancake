from api_clients.pet_client import PetClient
from config.pet_payloads import generate_random_pet


def test_post_pet():
    new_pet = generate_random_pet()

    response = PetClient.create_pet(new_pet)
    assert response.status_code == 200, f"Failed to create pet: {response.text}"

    response_json = response.json()
    assert response_json["name"] == new_pet["name"], "Pet name doesn't match"
    assert response_json["category"]["name"] == new_pet["category"]["name"], "Pet category doesn't match"


def test_get_pet(created_pet):
    response = PetClient.get_pet(created_pet)
    assert response.status_code == 200
    assert response.json()["id"] == created_pet


def test_put_pet(created_pet):
    old_body = PetClient.get_pet(created_pet).json()
    updated_body = PetClient.update_pet(created_pet)
    body_in_response = PetClient.get_pet(created_pet).json()

    assert old_body["id"] == body_in_response["id"], "The ID should remain the same after the update"
    assert old_body != body_in_response, "The data should change after the update"
    assert updated_body == body_in_response, "The updated data should match what we sent"


def test_delete_pet():
    new_pet = generate_random_pet()
    response = PetClient.create_pet(new_pet)
    assert response.status_code == 200, f"Failed to create pet: {response.text}"

    response = PetClient.delete_pet(new_pet["id"])
    assert response.status_code == 200, f"Failed to delete pet: {response.text}"

    get_response = PetClient.get_pet(new_pet["id"])
    assert get_response.status_code == 404, "Pet should not exist after deletion"


def test_create_pet_duplicate():
    new_pet = generate_random_pet()

    response_1 = PetClient.create_pet(new_pet)
    assert response_1.status_code == 200, f"Expected 200, got {response_1.status_code}"

    response_2 = PetClient.create_pet(new_pet)
    assert response_2.status_code == 409, f"Expected 409, got {response_2.status_code}"


def test_delete_non_existent_pet():
    non_existent_pet_id = 10000000

    response = PetClient.delete_pet(non_existent_pet_id)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"