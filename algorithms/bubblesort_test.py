from bubble_sort import BubbleSort
import unittest
import random

def test_result_is_sorted(array):
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            return False
    return True

class TestBubbleSort(unittest.TestCase):

    def test_small_array(self):
        array = [4, 2, 5, 7, 8, 1]
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))

    def test_medium_array(self):
        array = [4, 2, 5, 7, 8, 1, 11, 3, 6, 14, 2, 4, 3, 1, 15, 2, 6]
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))

    def test_already_sorted(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))

    def test_inversely_sorted(self):
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))

    def test_with_negatives(self):
        array = [10, -4, 3, -3, 0, 2, 1]
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))

    def test_large_random_dataset(self):
        array = []
        for i in range(1000):
            array.append(random.randint(0,10000))
        bs = BubbleSort()
        result = bs.bubble_sort(array)
        self.assertTrue(test_result_is_sorted(result))
        
if __name__ == '__main__':
    unittest.main()
    