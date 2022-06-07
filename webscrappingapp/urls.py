from django.urls import include, path
from .views import ScrapView

urlpatterns = [
    path('scrap/', ScrapView.as_view(), name='scrap'),
]