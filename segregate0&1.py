def segregate0and1(arr, n):
    # Counts the no of zeros in arr
    count = 0

    for i in range(0, n):
        if (arr[i] == 0):
            count = count + 1

    # Loop fills the arr with 0 until count
    for i in range(0, count):
        arr[i] = 0

    # Loop fills remaining arr space with 1
    for i in range(count, n):
        arr[i] = 1


# Function to print segregated array
def print_arr(arr, n):
    print("Array after segregation is ", end="")

    for i in range(0, n):
        print(arr[i], end=" ")


# Driver function
arr = [ 1, 0, 0, 0,1,0,0]
n = len(arr)

segregate0and1(arr, n)
print_arr(arr, n)
