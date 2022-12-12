matrix = [[1,2,3],
		  [4,5,6],
		  [7,8,9]]

print("given matrix")
print(matrix)

rows = len(matrix)
col = len(matrix[0])


for i in range(0,rows):
	for j in range(i,col):
		if(i!=j):
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp

print("transpose")
print(matrix)


for i in range(0,rows):
	l = 0
	h = col-1
	while(l<h):
		temp = matrix[i][l]
		matrix[i][l] = matrix[i][h]
		matrix[i][h] = temp

		l = l+1
		h = h-1

print("rotated matrix")
print(matrix)

