import datetime
import zipfile
import os
import time
import logging

from django.utils import timezone

LOGGER = logging.getLogger(__name__)


def get_localtime_now():
    return timezone.now().astimezone(timezone.get_default_timezone())


def get_localtime_today():
    return timezone.now().astimezone(timezone.get_default_timezone()).date()


def get_utc_time_underscored():
    """ return UTC time as underscored, to timestamp folders """
    t = datetime.datetime.utcnow()
    return t.strftime('%Y_%m_%d_%H_%M_%S')


def mkdir_p(path):
    """ mkdir -p path """
    if not os.path.exists(path):
        os.makedirs(path)


def ftp_get_file(host, remote_name, local_path):
    """ get file remote_name from FTP host host and copied it inot local_path"""
    from ftplib import FTP
    f = FTP(host)
    f.login()
    fh = open(local_path, 'wb')
    f.retrbinary('RETR {0}'.format(remote_name), fh.write)
    fh.close()
    f.quit()
    LOGGER.info("Copied from host %s: %s => %s", host, remote_name, local_path)


def unzip_file(fname, dirname):
    """ unzip file fname into dirname """
    zf = zipfile.ZipFile(fname)
    zf.extractall(path=dirname)
    LOGGER.info("Unzipped %s => %s", fname, dirname)


def benchit(func):
    """ decorator to measure time """

    def wrap(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_end = time.time()
        delta = time_end - time_start
        LOGGER.info('Function %s took %.2f seconds', func.__name__, delta)
        return res

    return wrap


def parse_gtfs_date(value):
    year = int(value[0:4])
    month = int(value[4:6])
    day = int(value[6:8])
    return datetime.date(year, month, day)


def parse_bool(value):
    int_value = int(value)
    return True if int_value else False


def get_utc_now():
    return datetime.datetime.utcnow().replace(tzinfo=timezone.utc)


def md5_for_file(path, block_size=32768):
    """
    Block size directly depends on the block size of your filesystem
    to avoid performances issues
    Here I have blocks of 4096 octets (Default NTFS)
    """
    import hashlib
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def find_lastest_in_dir(dirname):
    def ctime_in_dirname(f):
        return os.path.getctime(os.path.join(dirname, f))

    if os.path.exists(dirname):
        files = os.listdir(dirname)
        if files:
            newest = max(os.listdir(dirname), key=ctime_in_dirname)
            return os.path.join(dirname, newest)
    return None
