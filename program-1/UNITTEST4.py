import unittest

from sort_array import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_empty_array(self):
        # Test sorting an empty array
        numbers = []
        sorted_numbers = sort_array(numbers)
        self.assertEqual(sorted_numbers, [])
    
    def test_sort_single_element_array(self):
        # Test sorting an array with a single element
        numbers = [1]
        sorted_numbers = sort_array(numbers)
        self.assertEqual(sorted_numbers, [1])
    
    def test_sort_sorted_array(self):
        # Test sorting an array that is already sorted
        numbers = [1, 2, 3, 4, 5]
        sorted_numbers = sort_array(numbers)
        self.assertEqual(sorted_numbers, [1, 2, 3, 4, 5])
    
    def test_sort_reverse_sorted_array(self):
        # Test sorting an array that is sorted in reverse order
        numbers = [5, 4, 3, 2, 1]
        sorted_numbers = sort_array(numbers)
        self.assertEqual(sorted_numbers, [1, 2, 3, 4, 5])
    
    def test_sort_random_array(self):
        # Test sorting a random array
        numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_numbers = sort_array(numbers)
        self.assertEqual(sorted_numbers, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
