from django.conf.urls import patterns, include, url


urlpatterns = patterns("",
  url(r"^$", "lazylight.views.index", name="index"),
  url(r"^update_relay$", "lazylight.views.toggle_relay", name="toggle_relay"),
)
