data = []

def bubble_sort(data):
    n = len(data)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data 
