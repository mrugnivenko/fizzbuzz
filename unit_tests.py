#!/usr/bin/python3

import unittest
from fizzbuzz import replace

class TestFizzbuzz(unittest.TestCase):
	def test_fizzbuzz(self):
		nums, A = [], []
		with open('tests.txt') as file:
			for line in file:
				nums.append(int(line[:line.find(' ')]))
				A.append(list(line[line.find(' ') + 1:]))
		for i in range(len(nums)):
			f = replace(nums[i])
			self.assertEqual(f, A[i])

if __name__=="__main__":
	unittest.main()
