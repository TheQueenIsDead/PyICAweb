# Celery tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.schedules import crontab
import logging
from pyica_web.celery import app as celery_app
from service.esi import EsiHandler


@celery_app.on_after_configure.connect
def setup_periodic_task(sender, **kwargs):
    # Sets up a periodic task
    sender.add_periodic_task(
        crontab(hour='*/1'),  # Executes every hour
        refresh_market_region_history.s(),
    )


@celery_app.task
def refresh_market_region_history():
    try:
        # TODO: Write refresh code
        pass
    except Exception as error:
        logging.warning(error)
        return False

    return True

