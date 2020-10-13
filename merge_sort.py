def merge_array(A,p,q,r):
    L=A[p:q+1]
    R=A[q+1:r+1] 
    i=j=0
    while i<len(L) and j<len(R):
        if  L[i] < R[j]:
            A[p]= L[i]
            i += 1
        else:
            A[p] = R[j]
            j += 1
        p +=1

    while i < len(L):
        A[p] = L[i]
        i+=1
        p+=1
    
    while j < len(R):
        A[p] = R[j]
        j+=1
        p+=1


def merge_sort(A,p,r):
    if p==r:
        return
    q=(p+r)//2
    merge_sort(A,p,q)
    merge_sort(A,q+1,r)
    merge_array(A,p,q,r)



A=[1,13,22,4,17,26,55,1]
merge_sort(A,0,18)
print(A)