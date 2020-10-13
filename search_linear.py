##asymptotic Analaysis
##   Linear search Algo 
## Does not depend other constant 
## depends on size of array
## worst case   [element is not exist]              -- o(n)  if n is very high than worst and average case running time is asymptotic
## best case    [element found at first position]
## average case [element found at middle of array]



def linear_search(arr,num):
    '''
    return index if element if found else return -1
    '''
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    else:
        return -1




#driver code
arr=[9,2,3,1,5,7,11,21,91]
num=int(input('Enter a number'))  ##take input from user
print(linear_search(arr,num))
