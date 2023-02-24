# Implement the bubble sort algorithm for an array of numbers


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return arr


arr = [64, 34, 25, 13, 22, 15, 1, 70]

bubbleSort(arr)
print("Sorted array is:", bubbleSort(arr))
