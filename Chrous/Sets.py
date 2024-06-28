my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(3)

# Iterating through a set
for item in my_set:
    print(item)

another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)
intersection_set = my_set.intersection(another_set)
difference_set = my_set.difference(another_set)
