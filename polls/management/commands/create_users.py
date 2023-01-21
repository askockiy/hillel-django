from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    description = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        if total < 1 or total > 10:
            raise ValueError('total must be between 1 and 10')

        faker = Faker()
        users = []
        for i in range(total):
            user = User(
                username=faker.first_name() + '_' + faker.last_name(),
                email=faker.email(),
                password=make_password(faker.password())
            )
            users.append(user)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created {} random users'.format(total)))
