# Exercise 7 (Second half)

# Question 3
# Implementation for both the original and optimized reverse functions
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current

    # Original implementation
    def original_reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # Optimized implementation
    def optimized_reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


# Timing code
import timeit
import random

# Test the performance of both methods
sizes = [1000, 2000, 3000, 4000]

for size in sizes:
    linked_list = LinkedList()

    for _ in range(size):
        linked_list.append(random.randint(1, 100))

    original_time = timeit.timeit(linked_list.original_reverse, number=100)
    optimized_time = timeit.timeit(linked_list.optimized_reverse, number=100)

    print(f"List size: {size}\nOriginal Time: {original_time}\nOptimized Time: {optimized_time}\n")





# Question 4
    import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get_element_at_pos(self, pos):
        current = self.head
        for _ in range(pos):
            current = current.next
        return current

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Original implementation
    def original_reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # Optimized implementation
    def optimized_reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

# Test the performance of both methods and plot the results
sizes = [1000, 2000, 3000, 4000]

original_times = []
optimized_times = []

for size in sizes:
    linked_list = LinkedList()

    for _ in range(size):
        linked_list.append(random.randint(1, 100))

    original_time = timeit.timeit(linked_list.original_reverse, number=100)
    optimized_time = timeit.timeit(linked_list.optimized_reverse, number=100)

    original_times.append(original_time)
    optimized_times.append(optimized_time)

# Plotting
plt.plot(sizes, original_times, label='Original')
plt.plot(sizes, optimized_times, label='Optimized')
plt.xlabel('List Size')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison: Original vs Optimized')
plt.legend()
plt.show()
