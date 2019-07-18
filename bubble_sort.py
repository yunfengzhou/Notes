def bubble_sort(alist):
	n = len(alist)
	# 通过分析发现：总共需要进行n-1轮冒泡过程，第1轮冒泡，需要比较n-1次，第2轮冒泡需要比较n-2次
	for i in range(n-1):# n-1轮冒泡过程
		for j in range(n-1-i):# 第n-1轮冒泡时i=(n-2),此时的j应该只比较1次（n-1-(n-2))=1
			if alist[j] > alist[j+1]:
				alist[j+1],alist[j] = alist[j],alist[j+1]


a = [15,66,19,36,2,46]
bubble_sort(a)
print(a)
