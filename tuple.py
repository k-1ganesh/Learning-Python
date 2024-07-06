#  Tuples are immutable means onces created they cant be changed . 
# show in ( ) bracket

tup = (1 , 3, 5, 5 , "ganesh" , True)

# checking element is in or not
if 'ganesh' in tup:
    print(True)
else:
    print(False)   


# Diffenrent methods on tuple

# Concatenation
tup1 = ( 1, 2, 3, "ganesh")
tup2 = (4,5,6,'tushar')
print(tup1 + tup2)

# Can i add and delete element from tuple ? 
# No because tuples are immutable . But can i still do by some trick ? Yes
# Just convert tuple into list -> apply operation -> convert back to tuple

# Adding element 
l1 = list(tup1)
l1.append("tushar")
tup1 = tuple(l1)
print(type(tup1)," ",tup1) # Yeah successfully able to change !!!


print(tup1.count('Ganesh')) # counts the occurance