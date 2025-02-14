from faker import Faker
import random


fake = Faker()

def generate_order_body():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": 4,
        "phone": fake.phone_number(),
        "rentTime": fake.random_int(min=1, max=7),
        "deliveryDate": fake.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": " ".join(fake.words(nb=10))[:24],
        "color": [
            "BLACK",
            "GREY"
        ]
    }



def register_new_courier():
    return {
        "login": fake.user_name(),
        "password": ''.join(random.choices('0123456789', k=4)),
        "firstName": fake.first_name()
    }


