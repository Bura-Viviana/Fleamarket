import os
import json
from django.core.management import BaseCommand, CommandError
from producers.models import Producers
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str)

    def handle(self, *args, **options):
        file_name_from_command_line = options.get('file')

        if not file_name_from_command_line:
            raise CommandError('File not found,please check the path!')
        if not file_name_from_command_line.endswith('.json'):
            raise CommandError('Import supports .json files only!')
        file_path_on_disk = os.path.join('data', file_name_from_command_line)
        try:
            with open(file_path_on_disk) as import_file:
                producers = json.load(import_file)
                print(f"producers from file: {producers}")

            for producer in producers:
                user_data = producer["user_info"]
                db_user = AuthUserModel.objects.create_user(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    username=user_data['user_name'],
                    password='123',
                    is_staff=1,
                )
                producer_picture = 'producers/default.jpg' if 'picture' not in producer else producer['picture']
                db_producer = Producers(
                    user=db_user,
                    about=producer['about'],
                    picture=producer_picture
                )
                db_producer.save()

        except FileNotFoundError as e:
            raise CommandError('File at %s was not found' % os.path.join('data', file_path_on_disk))



