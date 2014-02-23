#Laakman_1_7.py
'''Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column is set to 0.'''

a = [[1, 0], [2, 3]] #--> [[0, 0], [2, 0]]

b = [[1, 2, 0], [4, 0, 6], [7, 8, 9]] #--> [[0, 0, 0], [0, 0, 0], [7, 0, 0]]

def convert_column(m, r, c):
	for i, row in enumerate(m[r:]):
		m[i][c] = 0 
	print m
	return m 

def convert(matrix):
	for i, row in enumerate(matrix):
		for x, element in enumerate(row): 
			if element == 0: 
				matrix[i] = [0]*len(row) #set row to 0
				convert_column(matrix, i, x) #set column to 0
	return matrix

#print convert(a)

def convert(matrix):
	width  = len(matrix[0])
	height = len(a)

	for y, row in enumerate(matrix):
		for x, column_element in enumerate(row):
			if column_element == 0:
				if y == 0:
					matrix[y] = [0]*width
					for row in matrix[y+1:]:
						if matrix[y][x] == 0:
							row[x] = 0
				elif y != 0 and matrix[x-1][y-1] != 0:
					print "yes", x, y, matrix, matrix[x-1][y-1]
					matrix[y] = [0]*width			
	return matrix

print convert(b)





