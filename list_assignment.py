# create an empty list
my_list=[]

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at second position(index 1)
my_list.insert(1, 15)

# extend the list with another list
my_list.extend([50, 60, 70])

# remove the last element from the list
my_list.pop()

#sort the list in ascending order
my_list.sort()

# find and print the index of 30
index_30 = my_list.index(30)
print("index of 30:", index_30)