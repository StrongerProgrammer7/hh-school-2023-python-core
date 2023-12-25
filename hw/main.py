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
market = Market(wines, beers)

print('Has drink by title test-------------------------------')
print(has_drink_by_title(market, 'Wine_1'))
print(has_drink_by_title(market, 'IPA'))
print('---------------------------------------------------------')

print('Get sorted drink by title ----------------------------')
list_sorted = market.get_drinks_sorted_by_title()
for drink in list_sorted:
    print(drink.title)
print('---------------------------------------------------------')
print('Get drink by date--------------------------------------')
list_drinks_inRange_year = market.get_drinks_by_production_date(2020, 2024)
for drink in list_drinks_inRange_year:
    print(drink.title, ' : ', drink.production_date)

print('------------------------------------------------------------')

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
