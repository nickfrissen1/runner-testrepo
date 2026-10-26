import unittest
from rekenen import optellen

class TestRekenen(unittest.TestCase):
    def test_optellen(self):
        self.assertEqual(optellen(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
