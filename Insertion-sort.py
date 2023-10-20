#Q: Perform Insertion Sort for a user inputted array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = eval(input("Enter the array: "))
insertion_sort(arr)
print("Sorted array is:", arr)
