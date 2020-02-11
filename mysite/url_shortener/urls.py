from django.urls import path
from .views import ShortenerView

app_name = 'shortener'
urlpatterns = [
    path('', ShortenerView.as_view(), name='shortener'),
]
