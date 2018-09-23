# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#列表
University=['CDTU','CDUT','CDIT','UESTC','SCU']

#在末尾增加元素
University.append('HUST')
print(University)
University.append('ZJU')

#修改元素
University[0]='HIT'
print(University)

#修改指定位置的元素
University.insert(2,'CDTU')
print(University)

#删除指定位置的元素
del University[2]
print(University)


#使用方法pop()删除元素
end=University.pop()
print(University)

#弹出列表中任何位置处的元素
which=University.pop(3)
print(which)

#根据值删除元素
University.remove('CDUT')
print(University)

#打印临时排序的列表
print(sorted(University))

#打印倒序临时排序的列表
print(sorted(University,reverse=True))

#列表永久排序
University.sort()
print(University)

#列表永久逆序排序
University.sort(reverse=True)
print(University)

University.reverse()
print(University)

Universities=len(University)
print(Universities)




