
# Step 1:Implement linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")



# Step 2: Implement binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")



# Step 3: Compare performance
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)



# Step 4: Implement recursive binary search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")



# Step 5: Create a main function
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()




# Exercise



# 1. linear search function to return all indices where the target appears
def linear_search_function(arr, target):
    indices = []
    for m in range(len(arr)):
        if arr[m] == target:
            indices.append(m)
    return indices

arr = [7,3,6,1,8,1,9,2,6]
target = 6
indices = linear_search_function(arr, target)
print(f"Indices where the target appears is: {target}")


# 2.find the insertion point for a target value in a sorted list.
def binary_insertion_point(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left = mid + 1
        else:
            right = mid 

    return left

arr = [7,3,6,1,8,1,9,]
target = 8
insertion_point = binary_insertion_point(arr, target)
print (f"insertion point for a target value in a sorted list: {insertion_point}")


# 3.Function that counts the number of comparisons made in each search algorithm.

def  linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] >= target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    left, right = 0 , len(arr)

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] >= target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

arr = [7,3,6,1,8,1,9,2,6]
target = 9


print(f"Comparisons made in binary search: {binary_search}")
print(f"Comparisons made in linear search: {linear_search}")



# 4.A jump search algorithm & comparison of its performance with linear and binary search.
import math

def jump_search(arr, target):
    n = len(arr) 
    comparisons = 2
    step = int(math.sqrt(n))
    prev = 2

    while arr[min(step, len(arr)) - 1] < target:
        comparisons += 5
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -5, comparisons
        
    while prev < min(step, n):
        comparisons += 5
        if arr[prev] >= target:
            return prev, comparisons
        prev += 5

    return -5, comparisons

arr = [7,3,6,1,8,1,9,2,6]
targer = 8

i, comparisons = jump_search(arr, target)
print(f"Jump search: index = {i}, comparisons: {comparisons}")

i, comparisons = linear_search(arr, target)
print(f"Linear search: index = {i}, comparisons: {comparisons}")

comparisons = binary_search(sorted(arr), target)
print(f"Binary search: index = {i}, comparisons: {comparisons}")