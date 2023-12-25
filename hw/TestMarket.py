import unittest
from wine import Wine
from beer import Beer
from market import Market

class TestMarketMethods(unittest.TestCase):
    def setUp(self):
        self.wines = [
            Wine("Merlot", 2018),
            Wine("Chardonnay", 2022),
            Wine("Cabernet Sauvignon", 2020),
        ]
        self.beers = [
            Beer("IPA", 2019),
            Beer("Stout", 2020),
            Beer("Lager", 2021),
        ]
        self.market = Market(self.wines,self.beers)

    def test_get_drinks_sorted_by_title(self):
        print('test_get_drinks_sorted_by_title')
        expected_order = [self.wines[2],self.wines[1],self.beers[0],self.beers[2],self.wines[0],self.beers[1]]
        actual_order = self.market.get_drinks_sorted_by_title()

        self.assertEqual(actual_order, expected_order)

    def test_has_drink_with_title_existing(self):
        print('test_has_drink_with_title_existing')
        self.assertTrue(self.market.has_drink_with_title("Chardonnay"))
        self.assertTrue(self.market.has_drink_with_title("IPA"))

    def test_has_drink_with_title_nonexistent(self):
        print('test_has_drink_with_title_nonexistent')
        self.assertFalse(self.market.has_drink_with_title("NonexistentWine"))
        self.assertFalse(self.market.has_drink_with_title("NonexistentBeer"))

    def test_get_drinks_by_production_date(self):
        print('test_get_drinks_by_production_date')
        expected_result = [
            self.wines[2],self.beers[0],self.beers[1],self.beers[2]
        ]

        actual_result = self.market.get_drinks_by_production_date(from_date=2019, to_date=2021)

        self.assertEqual(actual_result, expected_result)

    def test_get_drinks_by_production_date_no_range(self):
        print('test_get_drinks_by_production_date_no_range')
        expected_result = self.wines + self.beers
        actual_result = self.market.get_drinks_by_production_date()

        self.assertEqual(actual_result, expected_result)

    def test_get_drinks_by_production_date_one_from_range(self):
        print('test_get_drinks_by_production_date_one_from_range')
        expected_result = [self.wines[1]]
        actual_result = self.market.get_drinks_by_production_date(from_date=2022)

        self.assertEqual(actual_result, expected_result)

    def test_get_drinks_by_production_date_one_to_range(self):
        print('test_get_drinks_by_production_date_one_to_range')
        expected_result = [self.wines[0],self.beers[0]]
        actual_result = self.market.get_drinks_by_production_date(to_date=2019)

        self.assertEqual(actual_result, expected_result)
if __name__ == '__main__':
    unittest.main()
