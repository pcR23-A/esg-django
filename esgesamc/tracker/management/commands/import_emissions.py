# tracker/management/commands/import_emissions.py

import csv
from django.core.management.base import BaseCommand
from tracker.models import EmissionData
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import emissions data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file to import.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert the date and parse other fields
                date = parse_date(row['date'])
                kwh_usage = float(row['kwh_usage'])
                ng_usage = float(row['ng_usage'])
                gasoline_usage = float(row['gasoline_usage'])
                diesel_usage = float(row['diesel_usage'])
                total_emission = float(row['total_emission'])

                # Create and save the EmissionData instance
                EmissionData.objects.create(
                    date=date,
                    kwh_usage=kwh_usage,
                    ng_usage=ng_usage,
                    gasoline_usage=gasoline_usage,
                    diesel_usage=diesel_usage,
                    total_emission=total_emission,
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported emissions data.'))
