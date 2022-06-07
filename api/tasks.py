import csv
import logging
import os

from django.conf import settings

import requests
from celery import shared_task
from redis import ResponseError
from redisearch import Client, Query, TextField

logger = logging.getLogger(__name__)


ITEM_FIELDS = [
    TextField("title", weight=1.0),
    TextField("description", weight=1.0),
    TextField("image", weight=1.0),
]

client = Client("elements-cache", port=settings.REDIS_PORT, host=settings.REDIS_HOST)


@shared_task
def download_csv_file_to_cache():
    csv_url = os.environ.get("CSV_URL", None)
    if csv_url is not None:
        try:
            with requests.Session() as session:
                response = session.get(csv_url)
            decoded_content = response.content.decode("utf-8")

            csv_reader = csv.DictReader(decoded_content.splitlines(), delimiter=",")
            csv_contents = list(csv_reader)
        except requests.exceptions.RequestException as e:
            logger.info(f"An error occurred when downloading CSV content: {str(e)}")
            return False
        else:
            save_to_cache(csv_contents)
            logger.info("CSV Contents downloaded and saved to Cache")
            return True
    logger.info("Update CSV_URL environment variable")
    return False


def save_to_cache(items):
    if items:
        try:
            client.info()
            client.drop_index()
        except ResponseError:
            client.create_index(ITEM_FIELDS)
        for index, item in enumerate(items):
            client.add_document(
                index,
                title=item.get("title", ""),
                description=item.get("description", ""),
                image=item.get("image", ""),
            )

            logger.info(f"Item {index}: {item}")


def get_all_items_from_cache(per_result=20, offset=0):
    query = Query("*").paging(offset, per_result)
    res = client.search(query)
    return res.docs, res.total


def get_single_item(doc_id):
    res = client.load_document(doc_id)
    return res
