l1 = [43,12,65,3,2,1,1]

# List methods

l1.sort() # Sort the list in ascending order
l1.sort(reverse=True) # Sort the list in decending order

l1.reverse() # It reverses the string.
print(l1.count(1)) # Returns the count of element 

l2 = l1 # In this kind of operation l2 is reference to l1 . So changes did in l2 will affect l1
l2 = l1.copy() # This will resolve above issue

l1.append(15) # This method append the element in the last part of list
print(l1)

# l1.insert(Index , Element)
l1.insert(1,'Ganesh')
print(l1)  

print(l1+l2) # String concatenation
