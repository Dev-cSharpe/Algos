from sort_tester import array_sort_test
#selectio sort algo
# complexity Analsys 
# Worst   case : n^2
# Average case : n^2
# Best case   :  


def selection_sort(arr):
    '''

    '''
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


#driver code
arr=[1,11,2,22,3,44,4,9,0,12]
arr=selection_sort(arr)
print(arr)
print(array_sort_test(arr))