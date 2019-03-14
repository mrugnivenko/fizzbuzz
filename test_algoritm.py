import unittest
from algoritmimport is_3
from fizzbuzz import is_5
from fizzbuzz import is_3_or_5
from fizzbuzz import func

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz(self):
		vchod, vichod = [], []
		with open('tests.txt') as file:
			i = 0
			for line in file:
				if i % 2 == 0:
					vchod.append(line)
				if i % 2 == 1:
					vichod.append(line)
				i += 1
		for i in range(len(vchod)):
			f = func(vchod[i])
			self.assertEqual(f, vichod[i])

if __name__=="__main__":
	unittest.main()
