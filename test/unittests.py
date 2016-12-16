# encoding: utf-8

import unittest

import dothemath.operations as oper


class SimpleTests(unittest.TestCase):
    def setup(self):
        """
        Set up test datasets
        :return:
        """

    def tearDown(self):
        """
        Tear down test datasets
        :return:
        """

    def test_sum_001(self):
        var1 = 4
        var2 = 6
        self.assertEqual(oper.int_sum(var1, var2), 10)

    def test_sum_002(self):
        var1 = 9
        var2 = 2
        self.assertNotEqual(oper.int_sum(var1, var2), 5)

    def test_sum_003(self):
        var1 = 5.6
        var2 = 5
        with self.assertRaises(Exception) as _:
            oper.int_sum(var1, var2)

    def test_vec_001(self):
        vec1 = [1, 2, 3, 4]
        vec2 = [5, 3, 0, 2]
        self.assertListEqual(oper.matrix_sum(vec1, vec2), [6, 8])

    def test_vec_002(self):
        vec1 = [0, 1]
        vec2 = [-1, 0]
        self.assertListEqual(oper.matrix_sum(vec1, vec2), [-1, 1])

if __name__ == '__main__':
    unittest.main()
