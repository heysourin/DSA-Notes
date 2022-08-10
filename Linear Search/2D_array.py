def linearSearch (arr, target):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if (arr[i][j] == target):
				print("Position:",i,",",j)
	return [-1, -1]

arr = [[3, 12, 9], [5, 2, 89], [90, 45, 22]]
linearSearch(arr,45)
