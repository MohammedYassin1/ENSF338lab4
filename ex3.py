'''
1. The growth factor is done by rounding the capacity of the list to the nearest multiple of 4.
'''

#2.

import sys
import timeit

prev_capacity = 0
lst = []
import matplotlib.pyplot as plt

for i in range(64):
    lst.append(i)
    current_capacity = sys.getsizeof(lst)
    if current_capacity != prev_capacity:
        print(f"List capacity changed from {prev_capacity} bytes to {current_capacity} bytes when the list had {len(lst)} elements.")
        prev_capacity = current_capacity

#3.

lst = []
grow_s = []
grow_s1 = []

def grow_list(lst):
    lst.append(53)

for i in range(1000):
    lst = list(range(53))
    time = timeit.timeit(lambda: grow_list(lst),number=1)
    grow_s.append(time)

#4.

for i in range(1000):
    lst = list(range(52))
    time = timeit.timeit(lambda: grow_list(lst),number=1)
    grow_s1.append(time)


5.

plt.hist([grow_s, grow_s1], label=['s to s+1', 's-1 to s'])
plt.legend()
plt.xlabel('time')
plt.ylabel('Frequency')
plt.title('Histogram of Two Lists')
plt.show()

'''
It takes longer to grow from s-1 than from s. This is because the when the list grows from s-1 to s, new larger memory must be allocated and the 
contents of the list must be copied into the new memory. This is caused by the fact that there is enough capacuty to grow the list, which is not
the case when the list grows from s to s+1.
'''