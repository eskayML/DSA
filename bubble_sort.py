def bubble_sort(array):
   '''
      Sorts an array by bubbling each adjacent elements of the array, and then pushing the smaller one to the left

   '''
   size = len(array)
   for i in range(1,size):
      for j in range(size-1):
         if array[j] > array[j+1]:
            # Swaps the elements 🙂
            array[j], array[j+1] = array[j+1] ,array[j]



list = [200, 1, 32, 4, -100, 20, 50, 3, 234, 2343, 238234, 2, 5,3, 2,4]
bubble_sort(list)
print(list)

