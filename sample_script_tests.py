import unittest
from sample_script import *

class BasicFunctionTest(unittest.TestCase):
    def test_merge_and_sort_basic_ints(self):
        list_1_in = [3,2,1]
        list_2_in = [10,11,5]
        ret_val = merge_and_sort_lists(list_1_in, list_2_in)
        expect = [1,2,3,5,10,11]

        self.assertListEqual(expect, ret_val,
                'Should merge and sort two numeric lists')	

    def test_matrix_multply(self):
        matrixA = [[1,2,3],[4,5,6]]
        matrixB = [[0,9],[8,7],[6,5]]
        ret_val = matrix_multiply(matrixA, matrixB)
        expect = [[34, 38],[76, 101]]

        self.assertListEqual(expect, ret_val,
                'Should multiply two matrices')


if __name__ == '__main__':
	unittest.main()
