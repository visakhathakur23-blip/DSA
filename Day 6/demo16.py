list1=[1,67,4,6,64,37]
list1.append([3,45,6,7])
list1.extend([2,4,56,67])
print(list1)
print(len(list1))
print(type(list1))
list1.insert(2,45)
print(list1)
list1.remove(37)
list1.pop(6)
print(list1)
# list1.clear()
# print(list1)
print(max(list1))
print(min(list1))

list2=[4,6,9,8,7,9,8,9,5,6]
print(list2.count(9))
print(list2.count(4))
list2.sort()
print(list2)
list2.reverse()
print(list2)
print(list2.index(6 ))
print(list2.index(9,1))


list_1=[4,5,6]
list_2=list_1

list_2.append(96)
print(list_1,id(list_1))
print(list_2,id(list_2))



lst1=[4,5,6]
lst2=lst1.copy()
lst2.append(96)
print(lst1,id(lst1))
print(lst2,id(lst2))

