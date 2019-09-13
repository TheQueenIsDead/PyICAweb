# Celery tasks here
from __future__ import absolute_import, unicode_literals

from celery import chain
from celery.schedules import crontab
import logging
from pyica_web.celery import app as celery_app
from service.esi import EsiHandler


@celery_app.on_after_finalize.connect
def populate_database():
    """
    Populates the import_calculator database
    """
    # This chain uses partial signatures, as seen below
    # (https://docs.celeryproject.org/en/latest/getting-started/next-steps.html#designing-workflows)
    chain(
        establish_esi_connection.s() |
        populate_type_table.s() |
        populate_region_table.s() |
        populate_region_market_history_table.s()
    )()


@celery_app.on_after_finalize.connect
def setup_periodic_task(sender, **kwargs):
    """
    Periodic task scheduler
    :param sender: Node name of the worker
    :param kwargs: Keyword Arguments
    :return:
    """
    sender.add_periodic_task(
        crontab(hour='*/1'),  # Executes every hour
        refresh_market_region_history.s(),
    )

@celery_app.task
def establish_esi_connection():
    return True

@celery_app.task
def populate_type_table(status):
    return True

@celery_app.task
def populate_region_table(status):
    return True

@celery_app.task
def populate_region_market_history_table(status):
    return True


@celery_app.task
def refresh_market_region_history():
    """
    Refresh Market Region History data
    """
    try:
        # TODO: Write refresh code
        pass
    except Exception as error:
        logging.warning(error)
        return False

    return True

