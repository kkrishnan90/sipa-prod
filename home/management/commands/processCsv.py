from django.core.management.base import BaseCommand
from django.conf import settings
from home.models import Members
import os 
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR / 'input_members.csv'), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:                                
                Members.objects.create(
                    founding_member=row[0],
                    name=row[1],
                    email=row[2],
                    phone=row[3],
                    family_size=int(row[4]),
                    membership_number=row[5])