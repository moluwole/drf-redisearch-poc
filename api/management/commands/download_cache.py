from django.core.management.base import BaseCommand

import six
from pyfiglet import figlet_format

from api.tasks import download_csv_file_to_cache

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None


def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(string, font=font), color))
    else:
        six.print_(string)


class Command(BaseCommand):
    help = "Downloads the CSV file as a stream and writes the values to Redis for Caching using Celery"

    def handle(self, *args, **options):
        log("DRF", color="green", figlet=True)
        log("Redisearch POC", color="green", figlet=True)
        log("Starting download of CSV to cache in background...", color="yellow")
        download_csv_file_to_cache.delay()
