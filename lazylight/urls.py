from django.conf.urls import patterns, include, url


urlpatterns = patterns("",
  url(r"^$", "lazylight.views.index", name="index")
)
