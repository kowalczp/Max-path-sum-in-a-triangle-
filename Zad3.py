
def maxSum(triangle, l, n): 
	for i in range(l-1, -1, -1): 
		for j in range(i+1): 

			if (triangle[i+1][j] > triangle[i+1][j+1]): 
				triangle[i][j] += triangle[i+1][j] 
			else: 
				triangle[i][j] += triangle[i+1][j+1] 

	return triangle[0][0]
with open("zadanie_4_triangle_big.txt") as fp:
    
    for count, line in enumerate(fp):
        triangle = [
    [
        int(num) for num in line.split()
    ] for line in fp.read().splitlines()
]
 
        
        x= len(triangle)
        y=x-1
        
        
        print(maxSum(triangle, y, y)+68)

