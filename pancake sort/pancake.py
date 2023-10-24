def flip(arr, k):
    # Reverse the first k elements of the array
    arr[:k] = arr[:k][::-1]

def find_max_index(arr, n):
    # Find the index of the maximum element in the first n elements of the array
    max_index = 0
    for i in range(n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    n = len(arr)
    while n > 1:
        # Find the index of the maximum element in the current array
        max_index = find_max_index(arr, n)
        
        # If the maximum element is not at the end of the array,
        # flip the sub-array to move the maximum element to the first position
        if max_index != n - 1:
            # Flip the sub-array to move the maximum element to the beginning
            flip(arr, max_index + 1)
            
            # Flip the entire array to move the maximum element to its correct position
            flip(arr, n)
        n -= 1
    return arr

# Example usage
if __name__ == "__main__":
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = pancake_sort(unsorted_array)
    print("Sorted array:", sorted_array)
