import random
from faker import Faker

fake = Faker('ko_KR') 

def generate_user():
    return {
        "name": fake.name(),
        "age": random.randint(1, 100),
        "country": fake.country()
    }

def generate_log(user_ids):
    pages = ["home", "product", "cart"]
    return {
        "user_id": random.choice(user_ids),
        "page": random.choice(pages)
    }