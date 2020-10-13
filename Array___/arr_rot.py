arr=[1,2,3,4,5,6,7,8]



key=arr[0]
for i in range(0,len(arr)-1):
    arr[i]=arr[i+1]

arr[len(arr)-1]=key

for i in arr:
    print(i)

