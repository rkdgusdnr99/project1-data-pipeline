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
    return {
        "user_id": random.choice(user_ids),
        "page": f"/{fake.slug()}"[:50]
    }

def generate_countries(country_name, new_code):
    regions = ["Asia","Europe","North America","South America","Africa","Oceania"]
    return {
        "code": new_code,
        "name": country_name,
        "region": random.choice(regions)
    }