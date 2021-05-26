from django import forms
from django.db import models
from producers.models import Producers, ProductCategories, Products


# class OrderBy(models.TextChoices):
#     COUNT_PRODUCTS_ASC = 'count_products_asc', 'Number of products - ascending'
#     COUNT_PRODUCTS_DESC = 'count_products_desc', 'Number of products - descending'


class SearchAndFilterProducers(forms.Form):
    # search_term = forms.CharField(max_length=255, required=False, label='Search by Category')
    # order_by = forms.ChoiceField(choices=OrderBy.choices, required=False, label='Order by')
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=(),
        required=False,
        label='Categories'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = ProductCategories.objects.all()
        categories_choices = tuple([(category.id, category.name) for category in categories])
        self.fields['categories'].choices = categories_choices

    def clean_categories(self):
        categories = self.cleaned_data.get('categories', [])

        try:
            categories = [int(category_id) for category_id in categories]
        except ValueError:
            raise forms.ValidationError('Ingredient IDs must be integers.')

        return categories

    def get_filtered_producers(self):
        if self.is_valid():
            desired_categories = self.cleaned_data.get('categories', [])
            if len(desired_categories) == 0:
                # we return ALL producers
                return Producers.objects.all()

            # get all products having desired_category
            print(desired_categories)
            expected_products = Products.objects.filter(category__in=desired_categories)

            desired_producers = []
            for product in expected_products:
                if product.owner not in desired_producers:
                    desired_producers.append(product.owner)
            print(desired_producers)

            return desired_producers
        else:
            # if anything was wrong with the forms (maybe?) we return ALL producers
            return Producers.objects.all().order_by('name')
