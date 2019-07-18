def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):# 最差的情况只要考虑n-1次就行了
        min_index = i

        for j in range(i+1,n):# i+1代表从已知元素右侧开始对比，并且这个循环对各元素进行比较，将数值较小的下标传给min_index
            if arr[min_index]>arr[j]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index],arr[i]# 交换数值大小


a = [5,4,3,2,1,0]
selection_sort(a)
print(a)