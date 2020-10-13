from sort_tester import array_sort_test



def insertion_sort(arr):
    '''
    insertion sort : complexity ---> o(n^2)
    '''
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr                 



#driver code
arr=[64,25,12,22,11]
result=insertion_sort(arr)
print(result)
print(array_sort_test(arr))


#first  run
#   [25,64,12,22,11]
#second run
#   [25,12,64,22,11]
#   [12,25,64,22,11]
# third run
#   [12,25,22,64,11]
#   [12,22,25,64,11]
#forth run
#   [11,12,22,25,64]