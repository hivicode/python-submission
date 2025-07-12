import random

class Sort:
    def __init__(self):
        pass
    
    def bubble_sort(self, arr):
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            print(f"Proses array iterasi ke {i+1}: {arr_copy}")
            swapped = False
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    swapped = True
            if not swapped:
                break
        return arr_copy
    
    def selection_sort(self, arr):
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        for i in range(n):
            print(f"Proses array iterasi ke {i+1}: {arr_copy}")
            min_idx = i
            for j in range(i + 1, n):
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        return arr_copy
    
    def insertion_sort(self, arr):
        arr_copy = arr.copy()
        
        for i in range(1, len(arr_copy)):
            print(f"Proses array iterasi ke {i}: {arr_copy}")
            key = arr_copy[i]
            j = i - 1
            while j >= 0 and arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            arr_copy[j + 1] = key
        return arr_copy
    
    def merge_sort(self, arr):
        arr_copy = arr.copy()
        
        if len(arr_copy) <= 1:
            return arr_copy
        
        print(f"Proses array: {arr_copy}")
        mid = len(arr_copy) // 2
        left = arr_copy[:mid]
        right = arr_copy[mid:]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def quick_sort(self, arr):
        arr_copy = arr.copy()
        
        if len(arr_copy) <= 1:
            return arr_copy
        
        print(f"Proses array: {arr_copy}")
        pivot = arr_copy[len(arr_copy) // 2]
        left = [x for x in arr_copy if x < pivot]
        middle = [x for x in arr_copy if x == pivot]
        right = [x for x in arr_copy if x > pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right) 