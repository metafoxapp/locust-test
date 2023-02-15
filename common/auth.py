import csv
from faker import Faker
from random import choice

fake = Faker()
users = []

with open('./storage/data/users.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in reader:
        users.append(row)


def pick_credential():
    credential = choice(users)
    return credential


def login(client):
    credential = pick_credential()
    response = client.post('/api/v1/user/login', None, {
        'username': credential[1],
        'password': credential[2]
    })

    token = response.json()['access_token']
    # set auth token.
    client.headers.setdefault('Authorization', 'Bearer ' + token)
    client.get('/api/v1/me')


def pick_user():
    return choice(users)
