# my_array = [64, 34, 25, 5, 22, 11, 90, 12]
# n = len(my_array)
# for i in range(n-1):
#     minvalue = i
#     for j in range(i+1,n):
#         if my_array[j] < my_array[minvalue]:
#             minvalue = j
#     min = my_array.pop(minvalue)
#     my_array.insert(i,min)
# print("my array is:",my_array)

# my_array = [64, 34, 25, 5, 22, 11, 90, 12]
# n= len(my_array)
# for i in range(n):
#     minval = i
#     for j in range(i+1,n):
#         if my_array[j] > my_array[minval]:
#             minval = j
#     my_array[i],my_array[minval] = my_array[minval],my_array[i]
# print("the list is :",my_array)




# Prractice 1 10/04/2025
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
print("this is the sorted bubble sort:",my_array)