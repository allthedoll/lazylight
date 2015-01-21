from django.shortcuts import render
from django.http import HttpResponse

from lazylight.hardware_controller import ToggleRelay


def index(request):
  return render(request, "index.html")


def toggle_relay(request):
  ToggleRelay.delay(request.POST.get("socket"))
  return HttpResponse("Submitted.")
