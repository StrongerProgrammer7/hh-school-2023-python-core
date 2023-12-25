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

    def has_drink_with_title(self, title=None) -> bool:
        if self.wines is not None:
            if title in self.wines:
                return True
        if self.beers is not None:
            if title in self.beers:
                return True

        return False

    def get_drinks_sorted_by_title(self) -> list:
        list_drinks = list()
        if self.wines is not None:
            list_drinks += list(self.wines.values())
        if self.beers is not None:
            list_drinks += list(self.beers.values())
        list_drinks = sorted(list_drinks, key=lambda x: x.title )
        return list_drinks

    def __getListObjectsByDate(self,drinks: dict, from_date,to_date):
        list_drinks = list()
        for drink in drinks.values():
            if Market._isBothDateExists(from_date, to_date):
                if Market._isDateDrinkInRange(drink, from_date, to_date):
                    list_drinks.append(drink)
            elif from_date is not None and drink.production_date >= from_date:
                list_drinks.append(drink)
            elif to_date is not None and drink.production_date <= to_date:
                list_drinks.append(drink)
        return list_drinks

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        if from_date is None and to_date is None:
            list_drinks = []
            if self.wines is not None:
                list_drinks += list(self.wines.values())
            if self.beers is not None:
                list_drinks += list(self.beers.values())
            return list_drinks

        list_drinks = self.__getListObjectsByDate(self.wines,from_date,to_date)
        list_drinks += self.__getListObjectsByDate(self.beers,from_date,to_date)
        return list_drinks