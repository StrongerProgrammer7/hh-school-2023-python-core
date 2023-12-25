class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {} if wines is None else {wine.title: wine for wine in wines}
        self.beers = {} if beers is None else {beer.title: beer for beer in beers}

    def has_drink_with_title(self, title=None) -> bool:
        if self.wines is not None and self.beers is not None:
            if title in self.wines or title in self.beers:
                return True

        return False

    def get_drinks_sorted_by_title(self) -> list:
        pass

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        pass
