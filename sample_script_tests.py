import unittest
from sample_script import merge_and_sort_lists

class BasicFunctionTest(unittest.TestCase):
	def test_merge_and_sort_basic_ints(self):
		list_1_in = [3,2,1]
		list_2_in = [10,11,5]
		ret_val = merge_and_sort_lists(list_1_in, list_2_in)
		expect = [1,2,3,5,10,11]

		self.assertListEqual(expect, ret_val,
		'Should merge and sort two numeric lists')	


if __name__ == '__main__':
	unittest.main()
