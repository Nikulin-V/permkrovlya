from django.urls import path

from homepage.views import HomeView, FileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('price-list/', FileView.as_view(file_name='ПРАЙС КРОВЛЯ 28.04.22.pdf'), name='pricelist'),
]
