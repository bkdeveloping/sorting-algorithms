
def merge(left, right):

	i=0
	j=0
	result=[]
	while (i<len(left) and j<len(right)):

		if (left[i]< right[j]):
			result.append (left[i])
			i+=1
		else:
			result.append (right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	return result

def mergeSort (lists):
	if (len(lists)<=1):
		return lists

	else:

	    mid= len(lists)//2
	    left= mergeSort(lists[:mid])
	    print(left)
	    right= mergeSort(lists[mid:])
	    return merge(left, right)

lists=[-5, 85, 4, 2, 7898, 1]
print(mergeSort(lists))	    


