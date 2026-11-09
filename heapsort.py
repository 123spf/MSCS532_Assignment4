def left(i):
    """Return the index of the left child for a 0-indexed array."""
    return 2 * i + 1

def right(i):
    """Return the index of the right child for a 0-indexed array."""
    return 2 * i + 2

def parent(i):
    """Return the index of the parent for a 0-indexed array."""
    return (i - 1) // 2

def max_heapify(arr, n, i):
    """
    Maintains the max-heap property.
    n is the current size of the heap.
    i is the index of the current node being evaluated.
    """
    largest = i
    l = left(i)
    r = right(i)

    # Check if left child exists and is greater than the parent
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Check if right child exists and is greater than the largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If the largest is not the parent, swap and recursively heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """Builds a max-heap from an unsorted array."""
    n = len(arr)
    # Start from the last non-leaf node and move up to the root
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """Sorts an array in-place using Heapsort."""
    n = len(arr)
    
    # Phase 1: Build the initial max-heap
    build_max_heap(arr)

    # Phase 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Swap the max element (at root 0) to the end of the current heap
        arr[i], arr[0] = arr[0], arr[i]
        # Restore the max-heap property on the reduced heap
        max_heapify(arr, i, 0)
    
    return arr