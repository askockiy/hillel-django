from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help_text = 'Delete users by id'

    def add_arguments(self, parser):
        parser.add_argument(
            'user_ids',
            nargs='+',
            type=int,
            help='List of user ids to delete'
        )

    def handle(self, *args, **kwargs):
        user_ids = kwargs['user_ids']
        if User.objects.filter(is_superuser=True, id__in=user_ids).exists():
            self.stdout.write(self.style.ERROR('Cannot delete superusers'))
            return
        User.objects.filter(id__in=user_ids).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted users with ids: {}'.format(user_ids)))
