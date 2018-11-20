from django.urls import path

from .views import AboutPageView, HomePageView, AuthorPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('author/', AuthorPageView.as_view(), name='author'),
]
