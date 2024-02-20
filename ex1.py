# Exercise 1
# Question 1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print(" -> ".join(map(str, elements)))


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.display()  # Output: 0 -> 1 -> 2 -> 3

linked_list.delete(2)
linked_list.display()  # Output: 0 -> 1 -> 3




# Question 2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node:
            current_node.next_node = current_node.next_node.next_node

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next_node
        print(" -> ".join(map(str, elements)))

    def binary_search(self, num):
        current_node = self.head
        while current_node:
            if current_node.data == num:
                return True
            elif current_node.data < num:
                current_node = current_node.next_node
            else:
                return False
        return False


# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.display()  # Output: 1 -> 2 -> 3 -> 5

print(linked_list.binary_search(3))  # Output: True
print(linked_list.binary_search(4))  # Output: False




# Question 3
class Array:
    def __init__(self):
        self.elements = []

    def append(self, num):
        self.elements.append(num)

    def binary_search(self, num):
        low, high = 0, len(self.elements) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == num:
                return True
            elif self.elements[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def display(self):
        print(" ".join(map(str, self.elements)))


# Example usage:
array = Array()
array.append(1)
array.append(2)
array.append(3)
array.append(5)
array.display()  # Output: 1 2 3 5

print(array.binary_search(3))  # Output: True
print(array.binary_search(4))  # Output: False



"""
Question 4
The complexity of binary search for linked lists is O(logn), where 'n' is the number of elements in the linked list.

In a linked list, direct access to an element by index is not possible as it is in an array. Therefore, binary search for linked lists is implemented by traversing the list and repeatedly dividing it into two halves, similar to binary search in arrays. The key factor is that each step of the binary search reduces the search space by half.

However, because linked lists do not allow for random access, and each step of the binary search involves traversing the list to find the middle element, the time complexity for each step is O(n) in the worst case. Therefore, the overall time complexity for binary search in a linked list is O(logn) * O(n), which simplifies to O(n*logn)
"""



# Question 5
import timeit
import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    # ... (previous LinkedList implementation)

    def binary_search(self, num):
        current_node = self.head
        while current_node:
            if current_node.data == num:
                return True
            elif current_node.data < num:
                current_node = current_node.next_node
            else:
                return False
        return False

class Array:
    # ... (previous Array implementation)

    def binary_search(self, num):
        low, high = 0, len(self.elements) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == num:
                return True
            elif self.elements[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

def measure_performance(data_structure, input_size):
    data = [random.randint(1, input_size * 2) for _ in range(input_size)]
    data_structure.elements = sorted(data)  # Sorting for binary search

    def search_operation():
        for _ in range(100):  # Perform 100 search operations for averaging
            num_to_search = random.randint(1, input_size * 2)
            data_structure.binary_search(num_to_search)

    time_taken = timeit.timeit(search_operation, number=1)
    return time_taken

input_sizes = [1000, 2000, 4000, 8000]

for size in input_sizes:
    linked_list = LinkedList()
    array = Array()

    linked_list_time = measure_performance(linked_list, size)
    array_time = measure_performance(array, size)

    print(f"Input Size: {size}")
    print(f"Linked List Binary Search Time: {linked_list_time:.6f} seconds")
    print(f"Array Binary Search Time: {array_time:.6f} seconds")
    print()



# Question 6 (code to plot the graphs)
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class LinkedList:
    # ... (previous LinkedList implementation)

    def binary_search(self, num):
        current_node = self.head
        while current_node:
            if current_node.data == num:
                return True
            elif current_node.data < num:
                current_node = current_node.next_node
            else:
                return False
        return False

class Array:
    # ... (previous Array implementation)

    def binary_search(self, num):
        low, high = 0, len(self.elements) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.elements[mid] == num:
                return True
            elif self.elements[mid] < num:
                low = mid + 1
            else:
                high = mid - 1

        return False

def measure_performance(data_structure, input_size):
    data = [random.randint(1, input_size * 2) for _ in range(input_size)]
    data_structure.elements = sorted(data)  # Sorting for binary search

    def search_operation():
        for _ in range(100):  # Perform 100 search operations for averaging
            num_to_search = random.randint(1, input_size * 2)
            data_structure.binary_search(num_to_search)

    time_taken = timeit.timeit(search_operation, number=1)
    return time_taken

input_sizes = [1000, 2000, 4000, 8000]

linked_list_times = []
array_times = []

for size in input_sizes:
    linked_list = LinkedList()
    array = Array()

    linked_list_time = measure_performance(linked_list, size)
    array_time = measure_performance(array, size)

    linked_list_times.append(linked_list_time)
    array_times.append(array_time)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linked_list_times, marker='o', label='Linked List')
plt.plot(input_sizes, array_times, marker='o', label='Array')

# Interpolate with quadratic functions
linked_list_fit = np.polyfit(input_sizes, linked_list_times, 2)
array_fit = np.polyfit(input_sizes, array_times, 2)

linked_list_curve = np.poly1d(linked_list_fit)
array_curve = np.poly1d(array_fit)

x_values = np.linspace(min(input_sizes), max(input_sizes), 100)

plt.plot(x_values, linked_list_curve(x_values), '--', label='Linked List Fit')
plt.plot(x_values, array_curve(x_values), '--', label='Array Fit')

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Performance')
plt.legend()
plt.grid(True)
plt.show()


