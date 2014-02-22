#Laakman_1_6.py

'''
Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. 

Can you do this in place?
'''

  
def rotate(matrix):
	width = len([matrix][0])-1
	copy = [[None for column in matrix] for row in matrix]
	for x, row in enumerate(matrix):
		for y, column in enumerate(row): 
			copy[y][width - x] = matrix[x][y]
	matrix = copy 
	return matrix


m         =	[[1, 2, 3], 	
			 [4, 5, 6], 	
			 [7, 8, 9]] 	

m_rotated = [[7, 4, 1],
			 [8, 5, 2],
			 [9, 6, 3]]

m2 = 		 [[1,   2,  3,  4],		
	 		  [5,   6,  7,  8], 	
	 		  [9,  10, 11, 12], 	
	 		  [13, 14, 15, 16]]		

m2_rotated = [[13,  9,  5,  1], 
			  [14, 10,  6,  2], 
			  [15, 11,  7,  3], 
			  [16, 12,  8,  4]]


assert rotate(m) == m_rotated

assert rotate(m2) == m2_rotated