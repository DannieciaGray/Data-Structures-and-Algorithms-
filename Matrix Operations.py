#Matrix Addition
import timeit
import sys 

def matrix_addition(a,b):
	n= len(a)
	
    #dynamic initialization of matrices
	c=[[0 for _  in range(n)]for _ in range(n)]  
	
	for i in range(n):
		for j in range(n):
			c[i][j] = a[i][j] +b[i][j]
	return c

#Function to test execution time and memory usage 
def analyze_matrix():
	
    #Tets different matrix sizes
	for size in [10,50,100]:  #n x n matrix
		
        #Create two n x n matrices of the given size (with sample data)
		matrix_1 = [[i + j for j in range(size)] for i in range(size)]
		matrix_2 = [[i - j for j in range(size)] for i in range(size)]
			   

		#Function to wrap the matrix addition call for timeit
		def test_addition():
			matrix_addition(matrix_1,matrix_2)

		#measure execution time using timeit module
		execution_time = timeit.timeit(test_addition,number=1)

		#measure memory usage using sys.getsizeof
		matrices_1_memory = sys.getsizeof(matrix_1)
		matrices_2_memory = sys.getsizeof(matrix_2)
		total_memory      = sys.getsizeof(matrices_1_memory+matrices_2_memory)


		#Print results 
		print(f"Matrix Size: {size} x {size}")
		print(f"Execution Time: {execution_time:.6f} seconds")
		print(f"Memory Used by Matrices:{total_memory} bytes")
		print("-"*40)

analyze_matrix()