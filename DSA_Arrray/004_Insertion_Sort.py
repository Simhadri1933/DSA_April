my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)
for i in range(1,n):
    insert_index = i
    CV = my_array.pop(i)
    for j in range(i-1,-1,-1):
        if my_array[j] > CV:
            insert_index = j
    my_array.insert(insert_index,CV)
print("sorted array:",my_array)



# # 2 SECOND approach
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(1,n):
#     insert_index = i
#     current_value = my_array[i]
#     for j in range(i-1, -1, -1):
#         if my_array[j] > current_value:
#             my_array[j+1] = my_array[j]
#             insert_index = j
#         else:
#             break
#     my_array[insert_index] = current_value

# print("Sorted array:", my_array)