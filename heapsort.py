def max_heapify(arr, n, i):
    """
    Restores the max-heap property for a subtree rooted at index i.
    Takes O(log n) time, as it traverses a single path down the heap's height.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Find the largest element among the root, left child, and right child
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and recursively heapify if the root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Transforms an unordered array into a valid max-heap.
    Takes O(n) time by calling max_heapify bottom-up.
    """
    n = len(arr)
    # Start from the last non-leaf node and move backward to the root
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heapsort(arr):
    """
    Sorts an array in-place using the Heapsort algorithm.
    Guarantees an O(n log n) worst-case time complexity.
    """
    # Handle empty or single-element arrays in O(1) time
    if len(arr) <= 1:
        return arr
        
    build_max_heap(arr)
    n = len(arr)
    
    # Repeatedly extract the maximum element and rebuild the heap
    for i in range(n - 1, 0, -1):
        # Swap the max element (root) to its final sorted position at the end
        arr[0], arr[i] = arr[i], arr[0]
        # Shrink the active heap size (represented by i) and restore the root
        max_heapify(arr, i, 0)
        
    return arr
