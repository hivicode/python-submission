class ShellSort:
    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()

    def sorter(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            print(f"Sorting tiap gap={gap}: {arr}")
            gap //= 2
        return 0
