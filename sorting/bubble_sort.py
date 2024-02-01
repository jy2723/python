
def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - 1):


      if array[j] > array[j + 1]:


        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

data = []
n = int(input("enter length of array:"))
for i in range(n):
    user_input = int(input("enter elements:"))
    data.append(user_input)

bubbleSort(data)

print('Sorted Array :')
print(data)