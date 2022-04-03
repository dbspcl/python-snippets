# Selection sort in Python
# Implemented using an array
# for each element in array (index step)
#  set min index to current step
#  loop through rest of array (step + 1 to size)
#   set min index if element less than current value at min index
#  swap current step and min index values 
# 
# Complexity O(n-squared)

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change '<' to '>' in the if statement
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
print('Unsorted Array:')
print(data)
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)