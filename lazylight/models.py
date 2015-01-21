from django.db.models import Model

from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import IntegerField


class Relay(Model):
  name = CharField(default="Relay", max_length=255)
  enabled = BooleanField(default=True)

  channel = IntegerField(unique=True)
  actuated = BooleanField(default=False)

  class Meta:
    db_table = "relay"
