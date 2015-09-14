import os
import logging

from django.conf import settings
from common import ot_utils

LOGGER = logging.getLogger(__name__)

MOT_FTP = "gtfs.mot.gov.il"
FILE_NAME = "israel-public-transportation.zip"
GTFS_DATA_DIR = os.path.join(settings.DATA_DIR, 'gtfs', 'data')


def download_gtfs_file(force=False):
    """ download gtfs zip file from mot, and put it in DATA_DIR in its own subfolder """
    import shutil
    time_suffix = ot_utils.get_utc_time_underscored()
    if not os.path.exists(GTFS_DATA_DIR):
        ot_utils.mkdir_p(GTFS_DATA_DIR)
    tmp_file = '/tmp/{0}_tmp.zip'.format(time_suffix)
    LOGGER.info('downloading GTFS to tmp file')
    ot_utils.ftp_get_file(MOT_FTP, FILE_NAME, tmp_file)
    if not force:
        tmp_md5 = ot_utils.md5_for_file(tmp_file)
        last_dir = ot_utils.find_lastest_in_dir(GTFS_DATA_DIR)
        if last_dir:
            was_success = os.path.exists(os.path.join(last_dir, 'success'))
            if not was_success:
                LOGGER.info('Last time was not success')
            else:
                last_file = os.path.join(last_dir, FILE_NAME)
                try:
                    last_md5 = ot_utils.md5_for_file(last_file)
                except Exception as e:
                    LOGGER.exception('failed in md5 for last file - ignoring')
                    last_md5 = 'error_in_md5'
                if last_md5 == tmp_md5:
                    LOGGER.info('Checksum is identical - removing tmp file')
                    os.remove(tmp_file)
                    return None

    LOGGER.info('Checksum is different or force -- copying')
    local_dir = os.path.join(GTFS_DATA_DIR, time_suffix)
    ot_utils.mkdir_p(local_dir)
    try:
        os.remove(os.path.join(GTFS_DATA_DIR,'latest'))
    except (IOError, OSError):
        pass
    os.symlink(local_dir, os.path.join(GTFS_DATA_DIR,'latest'))
    local_file = os.path.join(local_dir, FILE_NAME)
    shutil.move(tmp_file, local_file)
    ot_utils.unzip_file(local_file, local_dir)
    LOGGER.info('All gtfs files are in %s' % local_dir)
    return local_dir


def write_success():
    import common.ot_utils
    last_dir = ot_utils.find_lastest_in_dir(GTFS_DATA_DIR)
    with open(os.path.join(last_dir, 'success'), 'w') as fh:
        fh.write('success on %s\n' % common.ot_utils.get_utc_now().isoformat())


def clean_all():
    from django.apps import apps
    models = apps.get_app_config('gtfs').models.values()
    for model in models:
        LOGGER.info('deleting %s', model.__name__)
        model.objects.all().delete()


def create_all(dirname):
    clean_all()
    from .importer import Importer
    i = Importer(dirname)
    i.import_all()
