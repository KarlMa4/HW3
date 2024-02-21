import matplotlib.pyplot as plt
import timeit
import random

# https://www.geeksforgeeks.org/python-program-for-insertion-sort/


def insertionSort(arr):
    n = len(arr)  # Get the length of the array

    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        # Store the current element as the key to be inserted in the right position
        key = arr[i]
        j = i-1
        # Move elements greater than key one position ahead
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

# https://www.geeksforgeeks.org/python-program-for-merge-sort/


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def create_random_list(size):
    """
    Create a list of specified size with random integers.

    Parameters:
    - size (int): The size of the list to be created.

    Returns:
    - list: A list containing random integers.
    """
    return [random.randint(0, size) for _ in range(size)]


sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500]

insertion_sort_times_runs = [[] for _ in range(15)]
merge_sort_times_runs = [[] for _ in range(15)]
merge_faster_size = None
# Perform the sorting and timing in a loop
for run in range(15):
    for size_index, size in enumerate(sizes):
        random_list = create_random_list(size)
        # Measure Insertion Sort time
        start_time = timeit.default_timer()
        insertionSort(random_list.copy())
        insertion_sort_time = timeit.default_timer() - start_time
        insertion_sort_times_runs[run].append(insertion_sort_time)
        # Measure Merge Sort time
        start_time = timeit.default_timer()
        mergeSort(random_list.copy(), 0, size - 1)
        merge_sort_time = timeit.default_timer() - start_time
        merge_sort_times_runs[run].append(merge_sort_time)
        if insertion_sort_time < merge_sort_time:
            merge_faster_size = size

    plt.figure(figsize=(15, 6))
    plt.plot(sizes, insertion_sort_times_runs[run],
             label=f'Insertion Sort Run {run+1}', marker='o')
    plt.plot(sizes, merge_sort_times_runs[run],
             label=f'Merge Sort Run {run+1}', marker='o')
    if merge_faster_size is not None:
        plt.annotate(f'Merge faster\n(Size: {merge_faster_size})',
                     (merge_faster_size,
                      merge_sort_times_runs[run][sizes.index(merge_faster_size)]),
                     textcoords="offset points", xytext=(-15, 10), ha='center', color='red')
    plt.title(f'Runtime Comparison Run {run+1}')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')

plt.show()
