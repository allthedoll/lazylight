from lazylight.celery import celery_lazylight

from celery.utils.log import get_task_logger

from celery.signals import celeryd_init
from celery.signals import worker_shutdown


logger = get_task_logger(__name__)


@celery_lazylight.task
def ToggleRelay(relay):
  logger.warning("Hello World!")
