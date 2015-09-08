from django.core.management.base import BaseCommand, CommandError
import gtfs.utils
from cProfile import Profile


class Command(BaseCommand):
    def _handle(self, *args, **options):
        gtfs.utils.create_all('tmp_data/gtfs/data/latest/')

    def add_arguments(self, parser):
        parser.add_argument('--profile', action='store_true')

    def handle(self, *args, **options):
        if options['profile']:
            profiler = Profile()
            profiler.runcall(self._handle, *args, **options)
            profiler.dump_stats('parse_gtfs.prof')
        else:
            self._handle(*args, **options)
