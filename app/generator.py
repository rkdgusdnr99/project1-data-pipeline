import random

def generate_log():
	users = [1,2,3,4,5]
	pages = ["home", "product", "cart"]

	return {
		"user_id": random.choice(users),
		"page": random.choice(pages)
	}