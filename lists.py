# creating an empty list
my_list = []
# Append the following elements to my_list: 10, 20, 30, 40.
my_list = ['10', '20', '30', '40']
# Insert the value 15 at the second position in the list.
my_list.insert(1, '15')
# Extend my_list with another list: [50, 60, 70].
list = ['50', '60', '70']
my_list.extend(list)
# Remove the last element from my_list.
del my_list [-1]
# Sort my_list in ascending order.
my_list.sort()
# Find and print the index of the value 30 in my_list.
index_30 = my_list.index('30')
print(f"The index of 30 is: {index_30}")
