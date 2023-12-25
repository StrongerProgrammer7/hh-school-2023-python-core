import random

from wine import Wine
from beer import Beer
from market import Market

def work_with_more_objecs():
    beer_objects = []
    wine_objects = []

    for i in range(1, 101):
        beer_title = f"Beer_{i}"
        beer_production_year = random.randint(2000, 2022)
        beer_objects.append(Beer(beer_title, beer_production_year))

        wine_title = f"Wine_{i}"
        wine_production_year = random.randint(2000, 2022)
        wine_objects.append(Wine(wine_title, wine_production_year))

    market = Market(wine_objects, beer_objects)
    print(market.has_drink_with_title('Wine_2'))
    print(market.has_drink_with_title('Wine_5'))
    print(market.has_drink_with_title('Wine_103'))

def work_with_less_objects():
    beers = [
        Beer("Stout", 2020),
        Beer("IPA", 2019),
        Beer("Lager", 2021)
    ]

    # Create 2 Wine objects with normal titles
    wines = [
        Wine("Merlot", 2018),
        Wine("Chardonnay", 2022)
    ]
    market = Market(wines, beers)
    print(market.has_drink_with_title('IPA'))
    print(market.has_drink_with_title('Wine_5'))

    print(market.get_drinks_sorted_by_title()[0][0])
work_with_less_objects()
"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
