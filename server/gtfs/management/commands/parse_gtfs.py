from django.core.management.base import BaseCommand, CommandError
import gtfs.utils

class Command(BaseCommand):
    def handle(self, *args, **options):
        gtfs.utils.create_all('tmp_data/gtfs/data/2015_09_07_17_00_12/')

