# Binary Search Algorithm
# WorstCase Time Complexity : O(logn)
 

def binary_search(arr,num):
    '''
    search an element 
    '''
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if num==arr[mid]:
            return mid
        elif num>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    else:
        return -1



#driver code
arr=[1,2,3,4,5,6,7,8,9]
print(binary_search(arr,8))