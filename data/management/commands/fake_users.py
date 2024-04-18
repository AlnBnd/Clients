from django.core.management.base import BaseCommand
import random
import string
from faker import Faker
from django.contrib.auth import get_user_model
from data.models import Client

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        def generate_fake_clients(num_clients):
            users = User.objects.all()
            for _ in range(num_clients):
                account_number = ''.join(random.choices(string.digits, k=8))
                last_name = fake.last_name()
                first_name = fake.first_name()
                middle_name = fake.first_name() 
                birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
                inn = ''.join(random.choices(string.digits, k=12))
                responsible_person = random.choice(users)
                status = random.choice([choice[0] for choice in Client.STATUS_CHOICES])
                Client.objects.create(account_number=account_number, last_name=last_name,
                                      first_name=first_name, middle_name=middle_name,
                                      birth_date=birth_date, inn=inn,
                                      responsible_person=responsible_person, status=status)


        generate_fake_clients(10)