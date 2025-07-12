import math

class Search:
    def __init__(self):
        pass
    
    def linear_search(self, arr, target):
        for i in range(len(arr)):
            print(f"Proses pencarian ke {i+1}: memeriksa indeks {i} dengan nilai {arr[i]}")
            if arr[i] == target:
                return i
        return -1
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(f"Proses pencarian: left={left}, right={right}, mid={mid}, nilai[mid]={arr[mid]}")
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def recursive_binary_search(self, arr, target, left=None, right=None):
        if left is None:
            left = 0
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        print(f"Proses pencarian rekursif: left={left}, right={right}, mid={mid}, nilai[mid]={arr[mid]}")
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.recursive_binary_search(arr, target, mid + 1, right)
        else:
            return self.recursive_binary_search(arr, target, left, mid - 1)
    
    def jump_search(self, arr, target):
        n = len(arr)
        if n == 0:
            return -1
        
        step = int(math.sqrt(n))
        prev = 0
        
        print(f"Proses jump search: step={step}")
        
        while prev < n and arr[min(step, n) - 1] < target:
            print(f"Melompat ke indeks {step}, nilai={arr[min(step, n) - 1]}")
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        print(f"Melakukan linear search dari indeks {prev} sampai {min(step, n)}")
        while prev < min(step, n):
            print(f"Memeriksa indeks {prev}, nilai={arr[prev]}")
            if arr[prev] == target:
                return prev
            prev += 1
        
        return -1
    
    def interpolation_search(self, arr, target):
        low, high = 0, len(arr) - 1
        
        while low <= high and target >= arr[low] and target <= arr[high]:
            if low == high:
                if arr[low] == target:
                    return low
                return -1
            
            pos = low + int(((high - low) * (target - arr[low])) / (arr[high] - arr[low]))
            print(f"Proses interpolation: low={low}, high={high}, pos={pos}, nilai[pos]={arr[pos]}")
            
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                low = pos + 1
            else:
                high = pos - 1
        
        return -1 