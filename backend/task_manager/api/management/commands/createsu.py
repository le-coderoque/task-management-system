import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists():
            User.objects.create_superuser(
                username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
                password=os.getenv('DJANGO_SUPERUSER_PASSWORD'),
                email=os.getenv('DJANGO_SUPERUSER_EMAIL'),
            )
            print('Django superuser created.')
