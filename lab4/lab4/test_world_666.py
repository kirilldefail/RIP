import unittesit
from unittest.mock import Mock

from pynput.keyboard import KeyCode

from hero_builder import menu, HeroBuilder
from world import World

class TestWorld(unittest.TestCase):
    def setUp(self):
        builder = HeroBuilder()
        builder.set_name("L")
        builder.add_gun()
        builder.add_magic()
        builder.add_sword()
        self.menu = Mock(return_value = builder)

        self.world = World(self.menu())
        self.world.on_press = Mock(return_value = "life goes on"

    def game(self):
        result = self.world.operation()
        self.assertIn("Fungal hero dies", result)

if __name__ == "__main__":
    unittest.main()
