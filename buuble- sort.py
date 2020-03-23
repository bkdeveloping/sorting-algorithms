lists = []
n= int(input("Enter no of elements : "))
for x in range (0, n):
    element = int (input("Enter the element : "))
    lists.append (element)

a=0
t=0
def swap(i, j):
    lists[i] , lists[j] = lists[j] , lists[i]
while (a<49):
    if (t==n-1):
        t=0
        continue


    else:
        if (lists[t]> lists[t+1]):
               swap(t, t+1)
               t=t+1
               a=a+1
        else:
               t=t+1
               a=a+1

print ("your swapped list is", lists)                      





