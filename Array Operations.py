#Sum of n numbers in an array 
import timeit
import sys 

#Function to calculate the sum of numbers in an array
def sum (a,n):
	sum = 0
	for i in range(n):
		sum+=a[i]
	return sum



#Function to test execution time and memory usage 
def analyze_array():
	#Tets different array sizes
	for size in [100,1000,10000,100000]:
		#Create an array of the given size 
		arr = list(range(size))

		#Function to wrap the sum call for timeit
		def test_sum():
			sum(arr,size)

		#measure execution time using timeit module
		execution_time = timeit.timeit(test_sum,number=1)

		#measure memory usage using sys.getsizeof
		array_memory = sys.getsizeof(arr)


		#Print results 
		print(f"Array Size: {size}")
		print(f"Execution Time: {execution_time:.6f} seconds")
		print(f"Memory Used by Array:{array_memory} bytes")
		print("-"*40)

analyze_array()
