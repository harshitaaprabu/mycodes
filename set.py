num_set={1,2,3,4,5,6,7,8,9,10}
# print(num_set)
num_set.add(0)
# print(num_set)
# num_set.clear()
# print(num_set)
odd_set={1,3,5,7,9,}
even_set={2,4,6,8,10,22}
# print(num_set.difference(odd_set).difference(even_set))
# print(odd_set.difference(even_set))
# print(odd_set.union(even_set))
# print(num_set.intersection(odd_set).intersection(even_set))
# print(num_set.issubset(odd_set))
# print(num_set.issuperset(even_set))
num_set.discard(0)
# print(num_set)
# print(odd_set.isdisjoint(even_set))
num_set.update(even_set)
print(num_set)