tuple1 = ("apple", "banana", "kiwi", "apple")
print(tuple1)

#for 1 item in tuple
tuple2 = ("apple",)
print(tuple2)

#append
list1 = list(tuple1)
list1.append("orange")
tuple1 = tuple(list1)
print(tuple1)

#remove
list2 = list(tuple1)
list2.remove("orange")
tuple1 = tuple(list2)
print(tuple1)