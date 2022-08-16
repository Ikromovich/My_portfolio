from django.urls import path
from main.views import *

urlpatterns = [
    path("",index,name="index"),
    path("portfolio/<int:id>/",portfolio,name="portfolio"),
    path("send_email/",send_email,name="send_email"),
]