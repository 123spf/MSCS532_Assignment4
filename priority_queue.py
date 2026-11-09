class Task:
    """
    Represents a single task in the scheduler.
    Holds required attributes: task_id, priority, arrival_time, and deadline.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task({self.task_id}, Priority: {self.priority})"


class MaxPriorityQueue:
    """
    A max-priority queue implemented using a binary max-heap.
    Utilizes a dictionary (hash map) to track task indices for O(1) lookups.
    """
    def __init__(self):
        self.heap = []
        self.task_indices = {} 

    # O(1) arithmetic operations for locating relatives in the array
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        """
        Swaps two tasks in the heap array and updates their indices in the dictionary.
        Runs in O(1) time.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        # Update the dictionary to reflect the new positions
        self.task_indices[self.heap[i].task_id] = i
        self.task_indices[self.heap[j].task_id] = j

    def max_heapify(self, i):
        """
        Maintains the max-heap property by floating a smaller element down the tree.
        Runs in O(log n) time based on the height of the heap.
        """
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        # Check if the left child exists and is greater than the current node
        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
            
        # Check if the right child exists and is greater than the largest found so far
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        # If the largest is not the current node, swap and continue heapifying downward
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def insert(self, task):
        """
        Inserts a new task into the priority queue.
        Runs in O(log n) time.
        """
        original_priority = task.priority
        # Temporarily assign negative infinity to match the textbook procedure
        task.priority = float('-inf')
        
        self.heap.append(task)
        current_index = len(self.heap) - 1
        self.task_indices[task.task_id] = current_index

        # Float the task up to its correct position using its actual priority
        self.increase_key(task.task_id, original_priority)

    def extract_max(self):
        """
        Removes and returns the task with the highest priority.
        Runs in O(log n) time.
        """
        if len(self.heap) < 1:
            return None
            
        max_task = self.heap[0]
        
        # Base case: only one task remains
        if len(self.heap) == 1:
            self.heap.pop()
            del self.task_indices[max_task.task_id]
            return max_task

        # Move the last leaf to the root and remove the extracted task from the tracking dictionary
        last_task = self.heap.pop()
        self.heap[0] = last_task
        self.task_indices[last_task.task_id] = 0
        
        del self.task_indices[max_task.task_id]

        # Restore the max-heap property from the root downward
        self.max_heapify(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        """
        Increases the priority of a specific task and restores the heap property.
        Runs in O(log n) time because dictionary lookup takes expected O(1) time.
        """
        i = self.task_indices[task_id]
        
        if new_priority < self.heap[i].priority:
            return 

        self.heap[i].priority = new_priority
        
        # Float the task up until it is no longer greater than its parent
        while i > 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            self.swap(i, self.parent(i))
            i = self.parent(i)


if __name__ == "__main__":
    pq = MaxPriorityQueue()
    
    pq.insert(Task("T1", 10, "08:00", "12:00"))
    pq.insert(Task("T2", 5, "08:05", "10:00"))
    pq.insert(Task("T3", 20, "08:10", "14:00"))
    
    print("Tasks inserted.")
    print("Increasing T2 priority to 25...")
    pq.increase_key("T2", 25)
    
    print("Extracting tasks in priority order:")
    while len(pq.heap) > 0:
        print(pq.extract_max())
