from django.core.management.base import BaseCommand, CommandError
import gtfs.utils


class Command(BaseCommand):
    help = 'Download gtfs file from MOT'

    def add_arguments(self, parser):
        parser.add_argument('--force', default=False, action='store_true')

    def handle(self, *args, **options):
        dirname = gtfs.utils.download_gtfs_file(force=options['force'])
        if dirname is None: # same same
            return
        gtfs.utils.create_all(dirname=dirname)
        gtfs.utils.write_success()
