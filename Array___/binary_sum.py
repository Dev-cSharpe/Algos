def bin_arr_sum(A,B):
    res=[0 for i in range(len(A)+1) ]
    carry=0
    for i in range(len(A)-1,-1,-1):
        sum = (A[i] + B [i] + carry)
        res[i+1] = sum % 2
        carry  = sum //2
    res[0]=carry
    return res
 
A=[1,1,1,0]
B=[1,0,1,0]
print(bin_arr_sum(A,B))
