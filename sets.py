my_set = set()

my_set.add(1)
my_set.add(6)
my_set.add("Ama")

print(my_set)

set1 = {1,2,3,4,5,6,7,8}
set2 = {7, 8, 9, 10, 11, 3, 12, 13}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)