import random
import time
import sys

# Increase recursion depth for deterministic quicksort's worst-case
sys.setrecursionlimit(2500)

# ==========================================
# 1. HEAPSORT IMPLEMENTATION (Chapter 6)
# ==========================================
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def max_heapify(arr, n, i):
    largest = i
    l = left(i)
    r = right(i)

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)
    return arr


# ==========================================
# 2. MERGE SORT IMPLEMENTATION (Chapter 2)
# ==========================================
def mergesort(arr):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


# ==========================================
# 3. QUICKSORT IMPLEMENTATION 
# ==========================================
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


# ==========================================
# BENCHMARKING SCRIPT
# ==========================================
def generate_datasets(n=1000):
    """Generates four distinct array distributions."""
    random_arr = [random.randint(0, 10000) for _ in range(n)]
    sorted_arr = sorted(random_arr)
    reverse_sorted_arr = sorted_arr[::-1]
    repeated_arr = [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    
    return {
        "Random Array": random_arr,
        "Sorted Array": sorted_arr,
        "Reverse Sorted Array": reverse_sorted_arr,
        "Repeated Array": repeated_arr
    }

def measure_time(sort_func, arr):
    # Create a copy so we don't sort in-place multiple times on the same reference
    arr_copy = arr.copy() 
    start_time = time.perf_counter()
    if sort_func.__name__ == 'heapsort':
        sort_func(arr_copy) # Heapsort is in-place
    else:
        arr_copy = sort_func(arr_copy) # Merge/Quick return new lists
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    n = 1000
    datasets = generate_datasets(n)
    
    algorithms = {
        "Heapsort": heapsort,
        "Merge Sort": mergesort,
        "Randomized Quicksort": randomized_quicksort
    }
    
    print(f"{'Distribution':<25} | {'Heapsort':<15} | {'Merge Sort':<15} | {'Quicksort':<15}")
    print("-" * 75)
    
    for name, data in datasets.items():
        results = [name]
        for algo_name, algo_func in algorithms.items():
            exec_time = measure_time(algo_func, data)
            results.append(f"{exec_time:.5f}s")
        print(f"{results[0]:<25} | {results[1]:<15} | {results[2]:<15} | {results[3]:<15}")
