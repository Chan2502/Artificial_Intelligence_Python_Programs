import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Generate a list of random numbers
def generate_random_list(n):
    return [random.randint(1, 100) for _ in range(n)]

# Sort the list and measure the time required
def sort_and_measure_time(arr):
    start_time = time.time()
    sorted_arr = quicksort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time

# Example usage
n = 1000  # Number of elements in the list
arr = generate_random_list(n)
sorted_arr, elapsed_time = sort_and_measure_time(arr)

print("Sorted list:", sorted_arr)
print("Time required:", elapsed_time, "seconds")
