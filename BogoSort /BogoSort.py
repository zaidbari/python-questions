import random

def is_sorted(arr):
    # Check if the array is sorted in non-decreasing order
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    attempts = 0  # Track the number of attempts to sort the array
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        if attempts % 1000 == 0:
            # Print a status update every 1000 attempts
            print(f"Attempt {attempts}: {arr}")
    
    print(f"Sorted in {attempts} attempts.")
    
if __name__ == "__main__":
    # Example usage:
    unsorted_list = [3, 1, 2, 5, 4]
    print("Unsorted list:", unsorted_list)
    bogo_sort(unsorted_list)
    print("Sorted list:", unsorted_list)
