from app.models import Item, Type, Season
import itertools
from typing import List, Dict, Tuple


class Combiner:
    def __init__(self, clothes: Item) -> None:
        self.clothes = clothes

    def __data_formatting(self) -> Dict[str, List[List[Item]]]:
        return {
            season.title: [
                [item for item in self.clothes.filter(type=item_type, season__title__icontains=season.title)]
                for item_type in Type.objects.all()
            ]
            for season in Season.objects.all()
        }

    def get_combinations(self) -> Dict[str, List[Tuple[Item]]]:
        clothes = self.__data_formatting()

        for season, items in clothes.items():
            combinations = [combination for combination in itertools.product(*items)]
            clothes[season] = combinations

        return clothes
