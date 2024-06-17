from django.urls import path,reverse
from . import views


urlpatterns = [
    # path("january",views.index),
    # path("february",views.feb),
    path("index",views.index,name="index"),
    path("<int:month>",views.redirectedView),
    path("<str:month>",views.monthly_challenge,name="monthly-challenges")
]