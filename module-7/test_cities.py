
import unittest
from city_functions import city_country


class CityCountryTest(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Does a city and country return the expected format?"""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
