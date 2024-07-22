ss = "Ganesh is Good boy"
# String slicing
print(ss[:5])
print(len(ss))

# String Methods 

print(ss.lower()) # Convert string into lower case
print(ss.upper()) # Convert string into upper case
print(ss.replace('Ganesh','Tushar')) # Used to replace some part of string
print(ss.find('ganesh')) # If string present return starting index else return -1
print(ss.split(' ')) # used to split the string . After splitting it return list of splitted parts
print(ss.capitalize()) # Make first letter of string only capital.
sss = 'aaaa'
print(sss.count('aa')) # Counts the occurance of the char/string in string. Counting is exclusive
print(ss.endswith('boy')) # check whether string ends with parameter string 
print(ss.startswith('ganesh')) # check whether string starts with parameter string

# Join() Method
l1 = ss.split()
# Join() Method is used to concate ele of list or tuple into single string with separator
# separator.join(list/tuple)
print('#'.join(l1))
