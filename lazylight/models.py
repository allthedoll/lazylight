from django.db.models import Model

from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import IntegerField

from django.dispatch import receiver
from django.db.models.signals import post_save

from lazylight.hardware_controller import ToggleRelay


class Relay(Model):
  name = CharField(default="Relay", max_length=255)
  enabled = BooleanField(default=True)

  channel = IntegerField(unique=True)
  actuated = BooleanField(default=False)

  class Meta:
    db_table = "relay"

@receiver(post_save, sender=Relay)
def RelayUpdated(sender, **kwargs):
  ToggleRelay.delay(relay=kwargs["instance"])
