# Write a Python program to implement a binary search algorithm without using recursion. Use an iterative approach to search for an element in a sorted list. 

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left bound
        else:
            right = mid - 1  # Adjust the right bound

    return -1  # Element not found

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target_element = 7
result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
