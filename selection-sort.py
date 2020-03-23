lists = []

t= int(input("Enter no of elements : "))
for x in range (0, t):
    element = int (input("Enter the element : "))
    lists.append (element)


i=0

while (i<t):
		

	n= lists.index(min(lists[i:t]))
	lists[i] , lists[n] = lists[n], lists[i]
	i=i+1

print ("your sorted list is", lists) 
