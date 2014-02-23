#Laakman_1_7.py
'''Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column is set to 0.'''


def convert_column(matrix, column_number):
	for i, row in enumerate(matrix):
		matrix[i][column_number] = 0 


def convert_row(matrix, row_number):
	matrix[row_number] = [0]*len(matrix[row_number])


def convert(matrix):
	columns = []
	rows    = []
	for y, row in enumerate(matrix):
		for x, column_element in enumerate(row):
			if matrix[y][x] == 0:
				columns.append(x)
				rows.append(y)

	for column in columns:
		convert_column(matrix, column)

	for row in rows: 
		convert_row(matrix, row)

	return matrix



a = [[1, 0], [2, 3]] 

b = [[1, 2, 0], [4, 0, 6], [7, 8, 9]] 


assert convert(a) == [[0, 0], [2, 0]]

assert convert(b) == [[0, 0, 0], [0, 0, 0], [7, 0, 0]]