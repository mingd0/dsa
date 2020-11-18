class BubbleSort: 
    
    def bubble_sort(self, array): 
        array = array
        sort_complete = False
        while not sort_complete: 
            sort_complete = True
            for i in range(len(array) - 1): 
                if array[i] <= array[i+1]:
                    continue
                else: 
                    x = array[i]
                    y = array[i+1]
                    array[i] = y
                    array[i+1] = x
                    sort_complete = False
        return array