from quick_sort import QuickSort
import unittest
import random
import statistics

def test_result_is_sorted(array):
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            return False
    return True

class TestQuickSort(unittest.TestCase):

    def test_swap(self):
        arr = [0, 1, 2]
        qs = QuickSort()
        qs.swap(arr, 0, 2)
        self.assertEqual(arr, [2, 1, 0])

    def test_median_of_three_known(self):
        arr = [1, 3, 5]
        qs = QuickSort()
        pivot_index = qs.pivot_med_of_three(arr, 0, (len(arr)-1))
        self.assertEqual(2, pivot_index)

    def test_median_of_three_random(self):
        arr = []
        qs = QuickSort()
        for i in range(10):
            arr.append(random.randint(0,100))
        ilow = 0
        ihigh = len(arr) - 1
        imid = (ilow + ihigh) // 2
        vals = [arr[ilow], arr[imid], arr[ihigh]]
        med = statistics.median(vals)
        pivot_index = qs.pivot_med_of_three(arr, ilow, ihigh)
        self.assertEqual(med, arr[pivot_index])
        self.assertLessEqual(arr[ilow], arr[imid])
        self.assertLessEqual(arr[ihigh], arr[imid])
    
    def test_small_array(self):
        array = [4, 2, 5, 7, 8, 1]
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))

    def test_medium_array(self):
        array = [4, 2, 5, 7, 8, 1, 11, 3, 6, 14, 2, 4, 3, 1, 15, 2, 6]
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))

    def test_already_sorted(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))

    def test_inversely_sorted(self):
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))

    def test_with_negatives(self):
        array = [10, -4, 3, -3, 0, 2, 1]
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))

    def test_large_random_dataset(self):
        array = []
        for i in range(1000):
            array.append(random.randint(0,10000))
        qs = QuickSort()
        result = qs.quick_sort(array, 0, (len(array)-1))
        self.assertTrue(test_result_is_sorted(result))
        
        
if __name__ == '__main__':
    unittest.main()
    
