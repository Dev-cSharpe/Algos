def array_sort_test(arr):
    '''
    if array is sorted than return True 
    else False
    '''
    is_sorted=True
    for index in range(len(arr)-1):
        if arr[index] > arr[index+1]:
            is_sorted=False
            break
    return is_sorted