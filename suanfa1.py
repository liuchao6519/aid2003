"""
1. 给你一个长度为n的数组，其中只有一个数字出现了奇数次，
其他均出现偶数次，问如何快速的找到这个数字。
"""
list1=[1,1,1,1,5,5,5,5,7,7,9,9,4,4,4,6,6,6,6]
set1=set(list1)
def find_number():
    count=0
    for i in set1:
        for r in list1:
            if i ==r:
                count+=1
        if count%2==0:
            count=0
        elif count%2!=0:
            return i
x=find_number()
print(x)
print("我真牛逼！")
