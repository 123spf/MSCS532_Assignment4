import math

class Task:
    """
    Represents an individual task in the scheduler.
    """
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority})"


class MaxPriorityQueue:
    """
    A max-priority queue implemented using a zero-indexed binary max-heap.
    """
    def __init__(self):
        self.heap = []
        # A dictionary to map task_id to its current index in the heap array.
        # This is necessary to perform increase_key in O(log n) time.
        self.index_map = {}

    def is_empty(self):
        """Returns True if the priority queue is empty."""
        return len(self.heap) == 0

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        """Swaps two elements in the heap and updates their index mapping."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.index_map[self.heap[i].task_id] = i
        self.index_map[self.heap[j].task_id] = j

    def _max_heapify(self, i):
        """Maintains the max-heap property by floating a node down."""
        largest = i
        l = self._left(i)
        r = self._right(i)
        n = len(self.heap)

        if l < n and self.heap[l].priority > self.heap[largest].priority:
            largest = l

        if r < n and self.heap[r].priority > self.heap[largest].priority:
            largest = r

        if largest != i:
            self._swap(i, largest)
            self._max_heapify(largest)

    def insert(self, task):
        """
        Inserts a new Task into the priority queue.
        Time Complexity: O(log n)
        """
        # Store original priority, assign -infinity, then increase to proper priority
        original_priority = task.priority
        task.priority = -math.inf
        
        self.heap.append(task)
        current_index = len(self.heap) - 1
        self.index_map[task.task_id] = current_index
        
        self.increase_key(task, original_priority)

    def extract_max(self):
        """
        Removes and returns the task with the highest priority.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise Exception("Heap underflow: Cannot extract from an empty priority queue.")
        
        max_task = self.heap[0]
        last_task = self.heap.pop()
        del self.index_map[max_task.task_id]
        
        if not self.is_empty():
            self.heap[0] = last_task
            self.index_map[last_task.task_id] = 0
            self._max_heapify(0)
            
        return max_task

    def increase_key(self, task, new_priority):
        """
        Increases the priority of an existing task and fixes the max-heap property.
        Time Complexity: O(log n)
        """
        if new_priority < task.priority:
            raise ValueError("New priority is smaller than the current priority.")
            
        task.priority = new_priority
        i = self.index_map[task.task_id]
        
        # Float the task up the tree as long as it's greater than its parent
        while i > 0 and self.heap[self._parent(i)].priority < self.heap[i].priority:
            parent_idx = self._parent(i)
            self._swap(i, parent_idx)
            i = parent_idx


# --- Scheduler Simulation ---
if __name__ == "__main__":
    print("--- Initializing Scheduler Simulation ---")
    scheduler = MaxPriorityQueue()

    tasks = [
        Task(task_id="T1", priority=10, arrival_time=0, deadline=5),
        Task(task_id="T2", priority=5, arrival_time=1, deadline=10),
        Task(task_id="T3", priority=20, arrival_time=2, deadline=3)
    ]

    print("\nInserting tasks into the priority queue...")
    for t in tasks:
        scheduler.insert(t)
        print(f"Inserted: {t}")

    print("\nIncreasing priority of T2 from 5 to 25...")
    scheduler.increase_key(tasks[1], 25)
    print(f"Task T2 updated: {tasks[1]}")

    print("\nExecuting tasks based on highest priority:")
    while not scheduler.is_empty():
        current_task = scheduler.extract_max()
        print(f"Executing: {current_task}")