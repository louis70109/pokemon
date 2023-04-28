import unittest

from pokemon.sprite import Pokemon

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "bulbasaur": {
                "num": 1,
                "name": "Bulbasaur",
                "types": ["Grass", "Poison"],
                "genderRatio": {"M": 0.875, "F": 0.125},
                "baseStats": {
                    "hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45
                }, "abilities": {"0": "Overgrow", "H": "Chlorophyll"},
                "heightm": 0.7,
                "weightkg": 6.9,
                "color": "Green",
                "evos": ["Ivysaur"],
                "eggGroups": ["Monster", "Grass"],
                "tier": "Illegal", "isNonstandard": "Past"
            }}

    def test_get_existing_pokemon(self):
        p = Pokemon()
        sprite = p.get('bulbasaur')
        self.assertEqual(sprite.name, self.test_data['bulbasaur']['name'])
        self.assertEqual(sprite.types, self.test_data['bulbasaur']['types'])
        self.assertEqual(sprite.eggGroups, self.test_data['bulbasaur']['eggGroups'])
        self.assertEqual(sprite.isNonstandard, self.test_data['bulbasaur']['isNonstandard'])

    def test_get_non_existing_pokemon(self):
        p = Pokemon()
        sprite = p.get('non_existing_pokemon')
        self.assertEqual(sprite, "Error: Pokemon 'non_existing_pokemon' not found")


if __name__ == '__main__':
    unittest.main()
