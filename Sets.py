# Sets is unordered collection of element which stores unique elements.
# Because sets are unordered so they can't be accessed using indexes

# We cant change individual elements because we cant access that element expicitly but still we can change using trick . 
# First delete that element and add new changed element.

s = {1,2,3,4,4,"ganesh"}
print(s)

for i in s:
    print(i)


# Different Sets Methods

s1 = {1,2,3,4,'Tushar'}
s2 = {4,3,'Ganesh','Tushar'}

print(s1.union(s2)) # Does the union of 2 sets
print(s1.intersection(s2)) # Does the intersectioin of 2 sets
print(s1.symmetric_difference(s2)) # Does the ring sum
print(s1.difference(s2)) # Does the - operation on sets
print(s1.isdisjoint(s2)) # check whether 2 sets are disjoint or not
print(s1.issubset(s2)) # check subset condition
print(s1.issuperset(s2)) # checks superset condition


s1.add('Kachare') # Adding single element to the set
print(s1)

s1.remove('Kachare') # Removes the specified element from the set
print(s1)

s1.pop() # This deletes 1 random element from the set.

del s2 # This is used to completly delete the set. Memory also gets deallocated from the variable

# checking item is  in set or not 
if 2 in s1:
    print('yo')
else:
    print('no')

# deleting all elements of set and making set empty
s1.clear()        