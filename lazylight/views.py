from django.shortcuts import render
from django.http import HttpResponse

from lazylight.hardware_controller import ToggleRelay


def index(request):
  ToggleRelay.delay(relay="")
  return render(request, "index.html")
