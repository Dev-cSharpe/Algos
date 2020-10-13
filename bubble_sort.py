from sort_tester import array_sort_test


#best and average case complexity : o(n^2)
#with isswapdone we can improve complexity
#of algorithm, in such cases where no much iteration
#required to sort beacuse array is already in sorted state

def bubble_sort(arr):
    swap_count=0
    for i in range(len(arr)):
        swap_count+=1
        isswapdone=0
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                isswapdone=1
        if isswapdone==0:
            break
    #print('swap_count',swap_count)
    return arr



#driver code
arr=[64,25,12,22,99,-1,121,222,11,1,222,1234,11]
result=bubble_sort(arr)
print(array_sort_test(arr))
print(result)