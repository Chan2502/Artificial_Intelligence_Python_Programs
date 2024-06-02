import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
def generate_elements(n):
    return [random.randint(1, 100) for _ in range(n)]


def sort_elements(elements):
    start_time = time.time()
    sorted_elements = quick_sort(elements)
    end_time = time.time()
    return sorted_elements, end_time - start_time


n = 100
elements = generate_elements(n)
sorted_elements, sorting_time = sort_elements(elements)

print("Original Elements:", elements)
print("Sorted Elements:", sorted_elements)
print("Sorting Time:", sorting_time, "seconds")
