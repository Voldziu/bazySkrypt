import random

from faker import Faker
import datetime
fake = Faker()

def generate_types(num):
    data = []
    for i in range(num):
        row = {
            'id': i,
            'name': fake.name()[:10]
        }
        data.append(row)
    return data

def generate_profiles(num):
    data = []
    for i in range(1,num+1):
        name_surname= fake.name().split()
        name =name_surname[0][:10]
        surname = name_surname[1][:10]
        print(name_surname)
        row = {
            'id': i,
            'name': name,
            'surname':surname,
            'description':fake.text(max_nb_chars=5000),
            'birthday':fake.date_of_birth(minimum_age=13),
            'dateofcreation': fake.date_this_century(),
            'sex': random.choice(["K","M"]),
            'faith':fake.text(max_nb_chars=20),
            'isactive':random.choice([True,False])
        }
        data.append(row)
    return data