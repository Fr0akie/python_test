def bubble_sort(alist):
    for i in range(len(alist) - 1):  # 循环次数
        for j in range(len(alist) - 1 - i):  # 比较次数
            if alist[j] > alist[j + 1]:  # 比较相邻两者的值
                alist[j], alist[j + 1] = alist[j + 1], alist[j]  # 左边的值较大则交换两者的值
    return alist  # 返还排序后的list


list1 = [45, 22, 8, 30, 9, 10, 7, 6, 5, 4]
print(bubble_sort(list1))
