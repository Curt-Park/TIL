class SelectionSort:
	def	__init__(self, comp = lambda x, y: x < y):
		self.comp = comp
		
	def swap(self, arr, i, j):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		
	def sort(self, arr):
		sorted_arr = arr.copy()
		n = len(arr)
		
		for i in range(n):
			min_idx = i
			for j in range(i, n):
				if self.comp(sorted_arr[j], sorted_arr[min_idx]):
					min_idx = j
			self.swap(sorted_arr, i, min_idx)
			
		return sorted_arr
		
		
if __name__ == '__main__':
	ascending_sort = SelectionSort()
	descending_sort = SelectionSort(comp=lambda x, y: x > y)
	arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert arr2 == ascending_sort.sort(arr1)
	assert arr1 == descending_sort.sort(arr2)
	print('well done!')
