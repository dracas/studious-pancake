import random
import string

def generate_random_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_pet():
    return {
        "id": random.randint(10000000, 99999999),
        "category": {
            "id": random.randint(100, 999),
            "name": random.choice(["Dogs", "Cats", "Birds", "Snakes"])
        },
        "name": generate_random_name().capitalize(),
        "photoUrls": [],
        "tags": [
            {
                "id": random.randint(100, 999),
                "name": random.choice(["Carnivorous", "Herbivores", "Omnivorous "])
            }
        ],
        "status": random.choice(["available", "pending", "sold"])
    }

def generate_update_payload(pet_id):
    return {
        "id": pet_id,
        "category": {
            "id": random.randint(100, 999),
            "name": random.choice(["Dogs", "Cats", "Birds", "Snakes"])
        },
        "name": generate_random_name().capitalize(),
        "photoUrls": [],
        "tags": [
            {
                "id": random.randint(100, 999),
                "name": random.choice(["Carnivorous", "Herbivores", "Omnivorous "])
            }
        ],
        "status": random.choice(["available", "pending", "sold"])
    }