# Bubble sort in Python
# Implemented using an array
# For each element in the array (index i)
#  Go through elements to the right (leaving at end those done so far, i.e. loop through length - i - 1), use index j
#   if array[j] > array[j+1] then swap them (quick 3-liner using a temp variable)
#
# Complexity O(n-squared)

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]
print('Unsorted Array:')
print(data)

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)