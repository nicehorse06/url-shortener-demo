from django.urls import path
from .views import ShortenerView

app_name = 'shortener'
urlpatterns = [
	path('<int:url_id>/', ShortenerView.as_view()),
    path('', ShortenerView.as_view(), name='shortener'),
]
