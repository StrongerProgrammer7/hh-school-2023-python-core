import random

from wine import Wine
from beer import Beer
from market import Market

beers = []
wines = []


def create_many_objects(years: tuple, count):
    global beers, wines
    for i in range(1, count):
        beer_title = f"Beer_{i}"
        beer_production_year = random.randint(years[0], years[1])
        beers.append(Beer(beer_title, beer_production_year))

        wine_title = f"Wine_{i}"
        wine_production_year = random.randint(2000, 2022)
        wines.append(Wine(wine_title, wine_production_year))


def has_drink_by_title(market: Market, title) -> bool:
    return market.has_drink_with_title(title)


def create_lessObjects():
    global beers, wines
    beers = [
        Beer("Stout", 2020),
        Beer("IPA", 2019),
        Beer("Lager", 2021)
    ]

    wines = [
        Wine("Merlot", 2018),
        Wine("Chardonnay", 2022)
    ]


create_lessObjects()
market = Market(wines,beers)

print(has_drink_by_title(market,'Wine_1'))
print(has_drink_by_title(market,'IPA'))



"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
