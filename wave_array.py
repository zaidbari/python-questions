def wave_array(array,n):
    if n%2==0:
        for i in range (0,n,2):
            array[i],array[i+1] = array[i+1], array[i]

    else:
        for i in range (0,n-1,2):
            array[i],array[i+1] = array[i+1], array[i]

array = [1,2,3,4,5]
n = len(array)
print("Before tansformation: ")
print(array)
wave_array(array,n)
print("After transformation: ")
print(array)