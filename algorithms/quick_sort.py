class QuickSort:

    def quick_sort(self, array, start, end):
        if (start < end):
            pivot_index = self.partition(array, start, end)
            self.quick_sort(array, start, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, end)
        return array

    def partition(self, array, start, end):
        # pivot = array[self.pivot_right(array, start, end)]
        pivot = array[self.pivot_med_of_three(array, start, end)]
        pivot_index = start
        for i in range(start, end):
            if array[i] <= pivot:
                self.swap(array, i, pivot_index)
                pivot_index += 1
        self.swap(array, pivot_index, end)
        return pivot_index
            
    """
    Returns index of pivot, if rightmost index is used
    """
    def pivot_right(self, array, start, end):
        return end

    """
    Returns index of pivot if median of three method is used
    """
    def pivot_med_of_three(self, array, start, end):
        mid = (start + end) // 2
        if array[mid] < array[start]:
            self.swap(array, mid, start)
        if array[end] < array[start]:
            self.swap(array, end, start)
        if array[mid] < array[end]:
            self.swap(array, end, mid)
        return end

    def swap(self, array, i, j):
        array = array
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
 
