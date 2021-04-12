import os
import json
from django.core.management import BaseCommand, CommandError
from producers.models import Products, ProductCategories
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
                products_list = json.load(import_file)
                print(f"products from file: {products_list}")

            for one_product in products_list:
                print(' ')
                owner = one_product["owner"]
                print(f'Processing producer: {owner}')
                db_user = AuthUserModel.objects.get(username=owner)

                category = one_product["category"]
                try:
                    db_category = ProductCategories(
                        name=category
                    )
                    db_category.save()
                    # If save() executed successfully, db_category is the new inserted cateory
                    print(f'Inserted category {category}')
                except:
                    # ALREADY EXISTS!!!
                    print(f'Category {category} already exists!')
                    # I need to read it from MySQL in order to use the existing category!
                    db_category = ProductCategories.objects.get(name=category)


                db_product=Products(
                    id_category=db_category,
                    id_owner=db_user,
                    name=one_product["name"],
                    description=one_product["description"],
                    unit=one_product["unit"],
                    quantity=one_product["stock"],
                    price=one_product["price"])
                db_product.save()

        except FileNotFoundError as e:
            raise CommandError('File at %s was not found' % os.path.join('data', file_path_on_disk))



