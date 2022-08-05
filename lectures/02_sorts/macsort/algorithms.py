from macsort.interface import SortAlgorithm


class BubbleSort(SortAlgorithm):
    # source: https://realpython.com/sorting-algorithms-python/
    def _sort(self, data: list[int]) -> list[int]:
        """Implement an in-place bubble sort"""
        n = len(data)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                self._incr()
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    already_sorted = False
            if already_sorted:
                break
        return data


class InsertionSort(SortAlgorithm):
    # source: https://realpython.com/sorting-algorithms-python/
    def _sort(self, data: list[int]) -> list[int]:
        """Implement an in-place insertion sort"""
        for i in range(1, len(data)):
            key_item = data[i]
            j = i - 1
            while j >= 0 and data[j] > key_item:
                self._incr()
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key_item
        return data


class MergeSort(SortAlgorithm):
    # source: https://realpython.com/sorting-algorithms-python/
    def _sort(self, data: list[int]) -> list[int]:
        if len(data) < 2:
            return data
        midpoint = len(data) // 2
        left_sorted = self._sort(data[:midpoint])
        right_sorted = self._sort(data[midpoint:])
        return self.__merge(left_sorted, right_sorted)

    def __merge(self, left: list[int], right: list[int]) -> list[int]:
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        result = []
        index_left = index_right = 0
        while len(result) < len(left) + len(right):
            self._incr(2)  # loop condition + upcoming if
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            self._incr()
            if index_right == len(right):
                result += left[index_left:]
                break

            self._incr()
            if index_left == len(left):
                result += right[index_right:]
                break
        return result


class QuickSort(SortAlgorithm):
    # source: https://www.geeksforgeeks.org/python-program-for-quicksort/
    def _sort(self, data: list[int]) -> list[int]:
        return self.__quicksort(0, len(data)-1, data)

    def __quicksort(self, left: int, right: int, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        self._incr()
        if left < right:
            pi = self.__partition(left, right, nums)
            self.__quicksort(left, pi-1, nums)
            self.__quicksort(pi+1, right, nums)
        return nums

    def __partition(self, left: int, right: int, nums: list[int]) -> list[int]:
        pivot, ptr = nums[right], left
        for i in range(left, right):
            self._incr()
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        nums[ptr], nums[right] = nums[right], nums[ptr]
        return ptr


class RadixSort(SortAlgorithm):
    # source https://www.geeksforgeeks.org/radix-sort/
    def _sort(self, data: list[int]) -> list[int]:
        if len(data) < 2:
            return data
        max1 = max(data)
        exp = 1
        while max1 / exp > 1:
            self._incr()
            self.__countingSort(data, exp)
            exp *= 10
        return data

    def __countingSort(self, arr: list[int], exp1: int):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            self._incr()
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
