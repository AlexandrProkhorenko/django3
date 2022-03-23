import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv") as f:
            phones = csv.DictReader(f, delimiter=';')
            for phone in phones:
                phone_object = Phone(

                    name=phone['name'],
                    price=phone['price'],
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug='-'.join(phone['name'].split()),
                )
                phone_object.save()





