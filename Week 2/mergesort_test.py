def merge(arr1, arr2):
    i1 = 0 # left array index
    i2 = 0 # right array index
    j = 0 # merged array index

def merge_sort(arr):
    n = len(arr)
    if len(arr) > 1:
        left_arr = arr[:n//2]
        right_arr = arr[n//2:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0


arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]