fruitList = ["Apple", "Banana", "Cherry"]
print(fruitList)
print(fruitList[0])
print(len(fruitList))

#duplication is allowed in list
fruitList = ["Apple", "Banana", "Cherry", "Apple"]
print(fruitList)
print(len(fruitList))
if "Apple" in fruitList:
    print("Yes, Apple is presnt in the list")
else:
    print("No, Apple is not present in the list")

#different datatypes
list1 = ["ariba", 19, True, "Female"]
print(list1)
print(type(list1))
#indexing can be negative
print(list1[-1])
#printing a Range
print(list1[1:3])
print(list1[:2])
print(list1[1:])
print(list1[-4:-1])

#change list items
fruitList[3] = "Kiwi"
print(fruitList)
fruitList[1:3] = ["Mango", "Pineapple"]
print(fruitList)

#insert
fruitList.insert(2 , "Banana") 
print(fruitList)

#Append
fruitList.append("Orange")
print(fruitList)

#Extend List
fruitList2 = ["melon", "watermelon", "guava"]
fruitList.extend(fruitList2)
print(fruitList)
newList = []
for x in fruitList:
    if "a" in x:
        newList.append(x)
print(newList)

#sort
fruitList.sort()
print(fruitList)

#remove
fruitList.remove("Banana")
print(fruitList)
fruitList.pop(6)
print(fruitList)
fruitList.pop()
print(fruitList)
del fruitList[1]
print(fruitList)
fruitList.clear()
print(fruitList)

