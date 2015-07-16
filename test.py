import unittest
from sort import sort_algorithm


class TestSort(unittest.TestCase):

    def test_sort_case1(self):
        data = ['car', 'truck', '8', '4', 'bus', '6', '1']
        sorted_data = sort_algorithm(data)
        self.assertEqual(
            sorted_data,
            ['bus', 'car', '1', '4', 'truck', '6', '8']
        )

    def test_sort_case2(self):
        data = ['1']
        sorted_data = sort_algorithm(data)
        self.assertEqual(sorted_data, ['1'])

    def test_sort_case3(self):
        data = ['car', 'truck', 'bus']
        sorted_data = sort_algorithm(data)
        self.assertEqual(sorted_data, ['bus', 'car', 'truck'])

    def test_sort_case4(self):
        data = ['8', '4', '6', '1', '-2', '9', '5']
        sorted_data = sort_algorithm(data)
        self.assertEqual(sorted_data, ['-2', '1', '4', '5', '6', '8', '9'])

    def test_sort_case5(self):
        data = ['car', 'truck', '8', '4', 'bus', '6', '1']
        sorted_data = sort_algorithm(data)
        self.assertEqual(
            sorted_data,
            ['bus', 'car', '1', '4', 'truck', '6', '8']
        )

    def test_sort_case6(self):
        data = ['car', '-999', '8', '888', 'bus']
        sorted_data = sort_algorithm(data)
        self.assertEqual(
            sorted_data,
            ['bus', '-999', '8', '888', 'car']
        )
    
    def test_sort_case7(self):
        data = ['12', '2', 'bus', '21']
        sorted_data = sort_algorithm(data)
        self.assertEqual(
            sorted_data,
            ['2', '12', 'bus', '21']
        )


if __name__ == '__main__':
    unittest.main()
