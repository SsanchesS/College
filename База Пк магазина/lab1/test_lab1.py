import unittest
from lab1 import *
class flipFirstElTest(unittest.TestCase):
    def test_data(self):
        self.assertEqual(flipFirstEl("3 4 1 2"),['2', '4', '1', '3'])
        self.assertEqual(flipFirstEl("Cлово Маша Пень"),['Пень', 'Маша', 'Cлово'])
        self.assertEqual(flipFirstEl("{2:2} [123,fas,gas] (21,41)"),['(21,41)', '[123,fas,gas]', '{2:2}'])

if __name__ == "__main__":
    unittest.main()