import random
import timeit
import matplotlib.pyplot as plt
#3.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

#4.
#linear_sort worst case: O(n) 
#binary_sort worst case: O(log(n))

#5.

lin = []
bin = []
sizes = [1000, 2000, 5000, 10000]
# Example usage:
for size in sizes:
    arr = random.sample(range(size), size)
    arr1 = arr

    x  = random.randint(1, size)

    l = timeit.timeit(lambda: linear_search(arr, x), number=100)
    lin.append(l)

    l = timeit.timeit(lambda: binary_search(arr1, x, 0, len(arr)), number=100)
    bin.append(l)



plt.scatter(sizes, lin, label = 'Linear Search', color = 'b')
plt.scatter(sizes, bin, label = 'Binary Search', color = 'r')
plt.legend()
plt.xlabel('trail')
plt.ylabel('time')
plt.title('Linear vs Binary Search')
plt.show()


