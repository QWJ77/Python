# 交集
'''
intersection（Iterable）
Iterable是可遍历对象
字符串：只判定字符串中的非数字
列表
元组
字典
集合
逻辑与“&”一样
集合里必须是个可哈希的值

intersection_update()
交集计算完毕后会再次赋值给原对象（即交集），会更改原对象！！！
只适用于可变集合
用可变集合和不可变集合操作时，谁在前面就以谁的类型为准，返回结果类型以运算符左侧为主
'''
# s1=frozenset([1,2,3,4,5])
# s2={4,5,6}
# # result=s1.intersection(s2)
# # result=s1&s2
# # result=s1.intersection_update(s2) #不可以，因为s1是不可变类型
# result=s2.intersection_update(s1)
# print(result,type(result))
# print(s1,s2)#集合本身并没边

# s1={"1","2","3","4","5"}
# print(s1.intersection("123")) #集合可以和字符串求交集
# print(s1.intersection(("1","2","6"))) #集合可以和元组求交集
# print(s1.intersection(["1","2","6"])) #集合可以和列表求交集
# print(s1.intersection(["1","2",["1","2"]])) #集合不能和不可哈希的对象求交集
# print(s1.intersection({"1":"abc","2":"12"})) #集合可以和字典求交集，求的是和key的交集

# 并集
'''
union()返回并集
逻辑或“|”
update()更新并集，会改变集合本身，所以只可用于可变集合
'''
s1={1,2,3}
# s1=frozenset([1,2,3])
s2={3,4,5}
# result=s1.union(s2)
# print(result,s1)
# result=s1|s2
# result=s1.update(s2)
# print(result,s1)

# 差集
'''
difference()
"-"
difference_update()
'''
s1={1,2,3}
s2={3,4,5}
result=s1-s2
print(result,s1)

# 判定操作
'''
isdisjoint()两个集合不相交
issuperset()一个集合包含另一个集合
issubset()一个集合包含于另一个集合
'''

# s1={1,2,3,4}
# s2={3,4,5}
# print(s1.isdisjoint(s2))