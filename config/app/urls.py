from unicodedata import name
from django.urls import path
from app.views import HomeView, ClothesListView, ClothesCombinationsView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("clothes", ClothesListView.as_view(), name="clothes"),
    path("clothes/combinations", ClothesCombinationsView.as_view(), name="clothes-combinations"),
]
