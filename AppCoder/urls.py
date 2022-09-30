from django.urls import path
from AppCoder.views import familiares



urlpatterns = [
    path('familia/', familiares),
]
