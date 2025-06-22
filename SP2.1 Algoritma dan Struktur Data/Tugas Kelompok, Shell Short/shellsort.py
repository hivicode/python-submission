class ShellSort:
    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()

    def sort(self, arr):
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
            gap //= 2
        return 0

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    print("Array sebelum pengurutan:")
    ShellSort.print_array(arr)

    ob = ShellSort()
    ob.sort(arr)

    print("Array setelah pengurutan:")
    ShellSort.print_array(arr)