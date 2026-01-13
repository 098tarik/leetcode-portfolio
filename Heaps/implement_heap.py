def parent(idx):
    if idx == 0:
        return -1
    return (idx - 1) // 2

def left_child(idx):
    return 2 * idx + 1

def right_child(idx):
    return 2 * idx + 2

class Heap():

    def __init__(self, higher_priority=lambda x,y: x < y, heap=None):
        self.heap = heap if heap is not None else []
        self.higher_priority = higher_priority
        if heap:
            self.heapify()
        
    def size(self):
        return len(self.heap)
    
    def top(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def push(self, elem):
        self.heap.append(elem)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, idx):
        if idx == 0:
            return
        parent_idx = parent(idx)
        if self.higher_priority(self.heap[idx], self.heap[parent_idx]):
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self.bubble_up(parent_idx)

    def pop(self):
        if not self.heap: return None
        top = self.heap[0]
        if len(self.heap) == 1:
            self.heap = []
            return top
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.bubble_down(0)
        return top
    
    def bubble_down(self, idx):
        left_i, right_i = left_child(idx), right_child(idx)
        is_leaf = left_i >= len(self.heap)
        if is_leaf:
            return 
        child_i = left_i

        if right_i < len(self.heap) and self.higher_priority(self.heap[right_i], self.heap[left_i]):
            child_i = right_i

        if self.higher_priority(self.heap[child_i], self.heap[idx]):
            self.heap[idx], self.heap[child_i] = self.heap[child_i], self.heap[idx]
            self.bubble_down(child_i)
        
    def heapify(self):
        for idx in range(len(self.heap) // 2, -1, -1):
            self.bubble_down(idx)

print("--- Test 1: Default Min-Heap ---")
h = Heap()
h.push(10)
h.push(5)
h.push(30)
h.push(2)

print(f"Top element: {h.top()}")  # Expected: 2

popped = []
while h.size() > 0:
    popped.append(h.pop())
print(f"Popped elements: {popped}")  # Expected: [2, 5, 10, 30]

print("\n--- Test 2: Heapify with existing list ---")
arr = [10, 5, 30, 2, 8]
h2 = Heap(heap=list(arr)) 
print(f"Top after heapify: {h2.top()}")  # Expected: 2

popped2 = []
while h2.size() > 0:
    popped2.append(h2.pop())
print(f"Popped elements: {popped2}")  # Expected: [2, 5, 8, 10, 30]

print("\n--- Test 3: Max-Heap with custom comparator ---")
h3 = Heap(higher_priority=lambda x, y: x > y)
h3.push(10)
h3.push(5)
h3.push(30)
h3.push(2)

print(f"Top element: {h3.top()}")  # Expected: 30

popped3 = []
while h3.size() > 0:
    popped3.append(h3.pop())
print(f"Popped elements: {popped3}")  # Expected: [30, 10, 5, 2]