
#Step 1: Implement Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)


#Step 2: Implement Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)




#Step 3: Implement Quick Sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)




#Step 4: Compare Performance


import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)




# Exercise

# 1.an in-place version of Quick Sort to improve its space efficiency.

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)

        # Recursively apply Quick Sort to the left and right subarrays
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choosing the rightmost element as the pivot
    pivot = arr[high]
    i = low - 1  # Pointer for the smaller element

    # Traverse through all elements
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return the partitioning index

# Example usage:
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)


# 2.Bubble Sort to stop early 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Initialize the swapped flag to False
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set the flag to True if a swap occurs
        if not swapped:
            # If no two elements were swapped, the array is sorted
            break

# Example usage:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)



# 3.a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Move elements of arr[left..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    # Create temporary arrays for merging
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]

    i = 0  # Initial index for left subarray
    j = 0  # Initial index for right subarray
    k = left  # Initial index for merged subarray

    # Merge the temp arrays back into arr[left..right]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Copy the remaining elements of left_half, if any
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Copy the remaining elements of right_half, if any
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def hybrid_merge_sort(arr, left, right, threshold=10):
    if right - left <= threshold:
        # Use Insertion Sort for small subarrays
        insertion_sort(arr, left, right)
    else:
        # Use Merge Sort for larger subarrays
        if left < right:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, threshold)
            hybrid_merge_sort(arr, mid + 1, right, threshold)
            merge(arr, left, mid, right)

# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    hybrid_merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)



# 4.a visualization of how each sorting algorithm works using a library like Matplotlib.
import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr, draw, pause):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
            # Draw the current state of the array
            draw(arr)
            time.sleep(pause)
        if not swapped:
            break

def draw(arr):
    plt.clf()  # Clear the current figure
    plt.bar(range(len(arr)), arr, color='blue')
    plt.ylim(0, max(arr) + 1)  # Set y-axis limit
    plt.title("Bubble Sort Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.pause(0.1)  # Pause to allow the plot to update

def main():
    # Example array to sort
    arr = np.random.randint(1, 100, size=20)  # Generate a random array
    print("Original array:", arr)

    plt.ion()  # Turn on interactive mode
    draw(arr)  # Initial drawing
    bubble_sort(arr, draw, pause=0.1)  # Sort the array with visualization
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Keep the final plot displayed

if __name__ == "__main__":
    main()