class InsertionSort: 
    
    def insertion_sort(self, array): 
        array = array
        for i in range(len(array)): 
            j = i
            while (j > 0 and array[j-1] > array[j]):
                tmp = array[j-1]
                array[j-1] = array[j]
                array[j] = tmp
                j -= 1
        return array
            