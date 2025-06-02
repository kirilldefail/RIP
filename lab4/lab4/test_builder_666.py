import unittest
from cell_builder import CellBuilder, Nature
from cell import Cell, State
from cell_states import CellStateA

class TestNature(unittest.TestCase):
    def setUp(self):
        self._nature = Nature()
        self._builder = CellBuilder()
        self._nature.builder = self._builder

    def test_build_animal_cell(self):
        self._nature.build_animal_cell()
        self.assertIn("Animal cell contains nucleus, membrane, mitochondrion, cytoplasm, centriole", self._builder.cell.__str__())
        self.assertIsInstance(self._builder.cell, Cell)

    def test_build_plant_cell(self):
        self._nature.build_plant_cell()
        self.assertIn("Plant cell contains nucleus, membrane, wall, mitochondrion, cytoplasm, centriole", self._builder.cell.__str__())

    def test_build_bacteria_cell(self):
        self._nature.build_bacteria_cell()
        self.assertIn("Bacterial cell contains membrane, wall, cytoplas", self._builder.cell.__str__())

    def test_build_fungal_cell(self):
        self._nature.build_fungal_cell()
        self.assertIn("Fungal cell contains nucleus, membrane, wall, mitochondrion, cytoplas", self._builder.cell.__str__())

if __name__ == "__main__":
    unittest.main()
