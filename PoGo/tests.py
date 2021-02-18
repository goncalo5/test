import unittest
from stats import get_base_stats, calc_stats, calc_stats_product, calc_cp
from pvp import get_max_stats_product


class TestStats(unittest.TestCase):

    def test_get_base_stats(self):
        self.assertEqual(get_base_stats(pokemon="excadrill"), (255, 129, 242))
        self.assertEqual(get_base_stats(pokemon=""), None)
        self.assertEqual(get_base_stats(pokemon="Charizard"), (223, 173, 186))

    def test_calc_stats(self):
        self.assertEqual(
            calc_stats(pokemon="excadrill", level=17, ivs=(2,15,15), _round=2),
            (141.55, 79.31, 141))
        self.assertEqual(
            calc_stats(pokemon="excadrill", level=28.5, ivs=(0,15,15), _round=2),
            (181.86, 102.70, 183))
        self.assertEqual(
            calc_stats(pokemon="groudon", level=13.5, ivs=(0,15,14), _round=2),
            (132.53, 119.28, 107))
        self.assertEqual(
            calc_stats(pokemon="groudon", level=51, ivs=(15,15,15), _round=2),
            (240.91, 205.41, 185))
        self.assertEqual(
            calc_stats(pokemon="", level=51, ivs=(15,15,15), _round=2),
            None)

    def test_calc_stats_product(self):
        self.assertEqual(
            calc_stats_product(pokemon="excadrill", level=17, ivs=(2,15,15)),
            1583.037)
        self.assertEqual(
            calc_stats_product(pokemon="groudon", level=13.5, ivs=(0,15,14)),
            1691.460)

    def test_calc_cp(self):
        self.assertEqual(
            calc_cp("excadrill", level=38, ivs=(12,15,15)),
            3116)
        self.assertEqual(
            calc_cp("excadrill", level=17, ivs=(2,15,15)),
            1499)
        self.assertEqual(
            calc_cp("groudon", level=13.5, ivs=(0,15,14)),
            1500)
        self.assertEqual(
            calc_cp("Rayquaza", level=40, ivs=(15,14,15)),
            3825)

class TestPVP(unittest.TestCase):
    def test_get_base_stats(self):
        self.assertEqual(get_max_stats_product(pokemon="excadrill", league="great"), 1583.037)
        self.assertEqual(get_max_stats_product(pokemon="excadrill", league="ultra"), 3417.738)

    def test_all_combinations(self):
        pokemons = [
            {
                "name": "primeape",
                "level": 24,
                "ivs": [6, 14, 15]
                "fast": "counter",
                "charged_1": "close combat",
                "charged_2": "night slash"
            },
            {
                "name": "Whiscash",
                "level": 26,
                "ivs": [11, 14, 15]
                "fast": "mud shot",
                "charged_1": "close combat",
                "charged_2": "night slash"
            },
            {
                "name": "primeape",
                "level": 24,
                "ivs": [6, 14, 15]
                "fast": "counter",
                "charged_1": "close combat",
                "charged_2": "night slash"
            },
            {
                "name": "primeape",
                "level": 24,
                "ivs": [6, 14, 15]
                "fast": "counter",
                "charged_1": "close combat",
                "charged_2": "night slash"
            },
        ]
        self.assertEqual(all_combinations(pokemons))

if __name__ == '__main__':
    unittest.main()