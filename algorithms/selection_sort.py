class SelectionSort:

    def selection_sort(self, array):
        n = len(array)
        for i in range(n-1):
            jmin = i
            for j in range(i+1, n):
                if array[j] < array[jmin]:
                    jmin = j
            if jmin != i:
                tmp = array[i]
                array[i] = array[jmin]
                array[jmin] = tmp
        return array
