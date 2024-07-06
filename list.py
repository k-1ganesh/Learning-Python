# check whether element is in list or not !
l1 = [1,2,3,4,5,'Ganesh']
if 1 in l1:
    print("Yes")
else:
    print("No")

print()

if 'Ganesh' in l1:
    print(True)

else:
    print(False) 


# List comprehentions 
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.  

# List = [Expression(item) for item in iterable if Condition] 

l1 = [i*i for i in range(5)]
print(l1) # creates the list of i*i from 0 to 4

l2 = [i**0.5 for i in l1 if i%2==1]
print(l2) # sqrt of only those element of l1 which are odd.

# Task 1 :  Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
ans = [i for i in names if i.find('o')!=-1] # Method 1
ans = [i for i in names if 'o' in i] # Method 2
print(ans)

# Task 2 : Accepts items which has more than 4 letters
ans1 = [i for i in names if len(i) > 4]
print(ans1)