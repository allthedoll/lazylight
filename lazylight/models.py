from django.db.models import Model

from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import IntegerField

from django.db.models.signals import post_save
from django.dispatch import receiver

from omnibus.api import publish


class Relay(Model):
  name = CharField(default="Relay", max_length=255)
  socket = IntegerField(unique=True)
  channel = IntegerField(unique=True)
  actuated = BooleanField(default=False)

  class Meta:
    db_table = "relay"


@receiver(post_save, sender=Relay)
def RelayUpdated(sender, **kwargs):
  publish(
      "lazylight", "update-relay",
      {"relay_pk": kwargs["instance"].pk,
       "actuated": kwargs["instance"].actuated})
