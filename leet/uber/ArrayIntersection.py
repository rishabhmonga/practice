def arrayIntersection(arr1, arr2):
	marker1 = marker2 = 0
	result = []
	while marker1 < len(arr1) and marker2 < len(arr2):
		if arr1[marker1] == arr2[marker2]:
			result.append(arr1[marker1])
			marker1 += 1
			marker2 += 1
		elif arr1[marker1] < arr2[marker2]:
			marker1 += 1
		else:
			marker2 += 1
	return result
	
def getIntersection(arr1, arr2):
	return arrayIntersection(arr1, arr2) if len(arr1) <= len(arr2) else arrayIntersection(arr2, arr1)
	
	
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print(arrayIntersection(arr1, arr2))