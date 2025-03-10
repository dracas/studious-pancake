import requests

from config.api_config import API_BASE_URL
from config.pet_payloads import generate_update_payload


class PetClient:
    @staticmethod
    def create_pet(payload):
        return requests.post(f"{API_BASE_URL}/pet", json=payload)

    @staticmethod
    def get_pet(pet_id):
        return requests.get(f"{API_BASE_URL}/pet/{pet_id}")

    @staticmethod
    def update_pet(pet_id):
        payload = generate_update_payload(pet_id)
        response = requests.put(f"{API_BASE_URL}/pet", json=payload)
        assert response.status_code == 200, f"Failed to update pet: {response.text}"
        return payload

    @staticmethod
    def delete_pet(pet_id):
        return requests.delete(f"{API_BASE_URL}/pet/{pet_id}")