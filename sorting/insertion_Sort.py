def insertion_Sort(array):
    for i in range(0, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j=j-1
        array[j+1] = key
data = []
n = int(input("enter length of array:"))
for i in range(n):
    user_input = int(input("enter elements:"))
    data.append(user_input)
insertion_Sort(data)
print('Sorted Array :')
print(data)