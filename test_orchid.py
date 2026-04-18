import unittest
from orchid import Orchid

class TestOrchid(unittest.TestCase):
    def test_bloom(self):
        o = Orchid("Test", "Blue", "TestLand")
        self.assertIn("blooms", o.bloom())

if __name__ == "__main__":
    unittest.main()
