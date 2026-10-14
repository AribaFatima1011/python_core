name = input(str("Enter name:"))
first_name = name[:name.index(" ")]
last_name = name[name.index(" ")+1:]
print(first_name[0], ". ", last_name[0],".")
print(name.upper())
listName = list(name)
print(listName.reverse)