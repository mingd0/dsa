import random
import datetime

class MergeSort:

    def mergeSort(self, array):
        n = len(array)
        if n < 2:
            return
        mid = n // 2
        left = array[0:mid]
        right = array[mid:len(array)]
        self.mergeSort(left)
        self.mergeSort(right)
        return self.merge(array, left, right)
        
    def merge(self, array, left, right):
        i = 0
        j = 0
        k = 0
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        while (i < len(left)):
            array[k] = left[i]
            i+=1
            k+=1
        while (j < len(right)):
            array[k] = right[j]
            j+=1
            k+=1
        return array

def main():
    array = []
    for i in range(1,1000):
        array.append(random.randint(0,10000))
    print(f'Unsorted: {array}\n')
    ms = MergeSort()
    print(f'Sorted: {ms.mergeSort(array)}')

if __name__ == "__main__":
    main()
