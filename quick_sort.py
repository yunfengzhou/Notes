def quick_sort(arr):
    if len(arr)>=2:
        mid = arr[len(arr)//2]
        left,right = [],[]
        arr.remove(mid)
        for num in arr:
            if num<mid:
                left.append(num)
            else:
                right.append(num)
        return quick_sort(left)+[mid]+quick_sort(right)
    else:
        return arr 

a = [15,66,19,36,2,46]

#这种方法的错误之处在于：quick_sort()代码中新建了list
#quick_sort(a)
#print(a)

print(quick_sort(a))
