def partion(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick(arr,low = 0,high = None):
    if high is None:
        high = len(arr)-1
        pivot_index = partion(arr,low,high)
        quick(arr,low,pivot_index-1)
        quick(arr,pivot_index+1,high)
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quick(my_array)
print("Sorted array:", my_array)