import requests

from config.api_config import API_BASE_URL


def test_post_adding_new_pet():
    url = f'{API_BASE_URL}/pet'
    payload = {
           "id":24564563456345665,
           "category":{
              "id":45,
              "name":"Snakes"
           },
           "name":"Bony",
           "tags":[
              {
                 "id":23,
                 "name":"Carnivorous"
              }
           ],
           "status":"available"
        }

    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bony"
    assert data["status"] == "available"