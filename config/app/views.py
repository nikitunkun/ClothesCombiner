from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import View, ListView
from app.models import Item
from app.service import Combiner
from typing import List, Dict, Tuple


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponseRedirect:
        return redirect("clothes")


class ClothesListView(ListView):
    model = Item
    ordering = ["type"]
    template_name = "app/clothes.html"
    context_object_name = "clothes"


class ClothesCombinationsView(ListView):
    model = Item
    template_name = "app/clothes_combinations.html"
    context_object_name = "clothes"

    def get_queryset(self) -> Dict[str, List[Tuple[Item]]]:
        obj = super().get_queryset()
        combiner = Combiner(clothes=obj.select_related("type").prefetch_related("season"))
        return combiner.get_combinations()
