#!/usr/bin/python3

import unittest
from fizzbuzz import is_3
from fizzbuzz import is_5
from fizzbuzz import is_3_or_5
from fizzbuzz import func

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz(self):
		vchod, vichod = [], []
		with open('tests.txt') as file:
			for line in file:
				nums.append(int(line[:line.find(' ')]))
				A.append(list(line[line.find(' ') + 1:]))
		for i in range(len(nums)):
			f = func(nums[i])
			self.assertEqual(f, A[i])

if __name__=="__main__":
	unittest.main()
