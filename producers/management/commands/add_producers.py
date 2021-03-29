from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from producers.models import Producer

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = AuthUserModel.objects.filter(producer=None).all()

        for user in users:
            p = Producer(user=user)
            p.picture = 'producers/default.jpg'
            p.save()

        print('Added to profile to %s users.' % len(users))
