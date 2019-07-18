def selection_sort(alist):
    # 与抓牌类似，左手上先有一张牌alist[0],然后抓一张牌alist[1]与手上的牌比较，value代表每次抓取的牌
    for i in range(1,len(alist)):
        value = alist[i]# 右手摸到的牌
        # while循环体套路
        j = i-1
        while j>=0:
            # 与手上左边的牌比较，如果比左边的牌小就交换位置
            if value<alist[j]:
                alist[j+1] = alist[j]
                alist[j] = value
            j = j-1
        


            # else:
            #         # 如果不满足条件了则表明排序已经结束
            #     break

a = [15,66,19,36,2,46]
selection_sort(a)
print(a)

