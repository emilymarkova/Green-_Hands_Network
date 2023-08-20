from django.urls import path
from .views import (main, detail, mission, forum)

urlpatterns = [
    path("", main, name="main"),
    path("detail/<slug>/", detail, name="detail"),
    path("mission", mission, name="mission"),
    path("forum/<slug>/", forum, name="forum"),
    # path('hitcount/', include('hitcount.urls', namespace='hitcount')),
]
