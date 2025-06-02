import unittest
from unittest.mock import Mock

from hero_states import HeroStateNothing, HeroStateMagic
from hero import Hero

class TestHeroStateNothing(unittest.TestCase):

    def setUp(self):
        self.mockHero = Mock()
        self.mockHero.name = "L"
        self.mockHero.cycle = iter([1,2,3]) 
        self.mockHero.transition_to = Mock(return_value = "Transition to HeroStateMagic")
        self.mockHero.go = Mock(return_value = "Hero L go...")

        self.state = HeroStateNothing()
        self.state.context = self.mockHero

    def test_fight(self):
        self.assertIn("Hero L hits the monster with his fists", self.state.fight())

    def test_change_state(self):
        self.assertEqual("Transition to HeroStateMagic", self.state.change_state())

if __name__ == "__main__":
    unittest.main()
