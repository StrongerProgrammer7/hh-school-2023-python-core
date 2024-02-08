from decorator import printing_decorator
class Market:
    @staticmethod
    def _isBothDateExists(from_date, to_date):
        return from_date is not None and to_date is not None

    @staticmethod
    def _isDateDrinkInRange(drink, from_date, to_date):
        return from_date <= drink.production_date <= to_date

    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {} if wines is None else {wine.title: wine for wine in wines}
        self.beers = {} if beers is None else {beer.title: beer for beer in beers}

    @printing_decorator
    def has_drink_with_title(self, title=None) -> bool:
        if title in self.wines:
            return True
        if title in self.beers:
            return True

        return False

    def __get_listDrinks(self,list_dict:list):
        list_drinks = list()
        for dict_drink in list_dict:
            list_drinks += list(dict_drink.values())

        return list_drinks

    #@printing_decorator
    def get_drinks_sorted_by_title(self) -> list:
        list_drinks = self.__get_listDrinks([self.wines,self.beers])
        list_drinks = sorted(list_drinks, key=lambda x: x.title)
        return list_drinks

    def __getDrinkByDate(self,from_date,to_date,drink):
        if self._isBothDateExists(from_date, to_date):
            if self._isDateDrinkInRange(drink, from_date, to_date):
                return drink
        elif from_date is not None and drink.production_date >= from_date:
            return drink
        elif to_date is not None and drink.production_date <= to_date:
            return drink
        return None

    def __getListObjectsByDate(self, drinks: dict, from_date, to_date):
        list_drinks = list()
        for drink in drinks.values():
            drinkByDate = self.__getDrinkByDate(from_date,to_date,drink)
            if drinkByDate is not None:
                list_drinks.append(drinkByDate)
        return list_drinks

    @printing_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        if from_date is None and to_date is None:
            return  self.__get_listDrinks([self.wines,self.beers])

        list_drinks = self.__getListObjectsByDate(self.wines, from_date, to_date)
        list_drinks += self.__getListObjectsByDate(self.beers, from_date, to_date)
        return list_drinks
