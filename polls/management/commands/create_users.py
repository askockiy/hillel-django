from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    description = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument(
            'total',
            type=int,
            help='Indicates the number of users to be created',
            choices=range(1, 11)
        )

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        faker = Faker()
        users = []
        for i in range(total):
            user = User(
                username=faker.first_name() + '_' + faker.last_name(),
                email=faker.email()
            )
            user.set_password(faker.password())
            users.append(user)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created {} random users'.format(total)))
