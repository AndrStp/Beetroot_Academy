"""
Task 2

Implement the mergeSort function without using the slice operator.
"""

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
  
        L =  [arr[i] for i in range(0, mid)] # L = arr[:mid]
        R =  [arr[i] for i in range(mid, len(arr))] # R = arr[mid:]
  
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
  
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is:", *arr, sep=' ')
    mergeSort(arr)
    print("Sorted array is: ", *arr, sep=' ')
