"""
list1 = [1, 2, 3, 4, "我爱你", [10, 20, 30]]
print(list1)
print(list1[4])
print(list1[5][1])

print(len(list1))

list2 = [1, 2, 3]
list3 = [10, 20, 30]

print(list2 + list3)
print(list3 * 2)

list4 = [1, 2, 3, 4, 5, 6, 7]

print(list4[0:3])
print(list4[-3:-1])
print(list4[-3:])
print(list4[::-1])
"""

# list5 = [1,2,3]
# del list5 # 在计算机内存中 a变量定义列表 删除
# print(list5)

# del list5[1] # 删除掉列表中指定的值
# print(list5)

# list5.append(4)
# print(list5)

# list5.insert(2,[20,30,40]);
# print(list5)

# list5.clear()
# print(list5)

# a = [20,30,40]
# list5 = list5 + a;
# list5.extend(a)
# print(list5)
# print(list5.copy())

# names = ["Bob", "Tom", "alice", "Jerry", "Wendy", "Smith"]
# new_names = [name.upper() for name in names if len(name) > 3 ]
# print(new_names);

a = (x for x in range(10))
print(a)
print(tuple(a))