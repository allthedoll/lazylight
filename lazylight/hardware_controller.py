from lazylight.celery import celery_lazylight

from celery.utils.log import get_task_logger

from celery.signals import celeryd_init
from celery.signals import worker_shutdown

from lazylight.models import Relay

from omnibus.api import publish


logger = get_task_logger(__name__)


@celery_lazylight.task
def ToggleRelay(new_relay_state):
  relay = Relay.objects.get(pk=new_relay_state.get("relay_pk"))
  relay.actuated = new_relay_state.get("actuate") == "true"

  # TODO: Implement wiringPi stuff here.

  logger.warn(
      "%s (socket %d): %s.", relay.name, relay.socket,
      "Actuated" if relay.actuated else "Deactuated")
  relay.save()
