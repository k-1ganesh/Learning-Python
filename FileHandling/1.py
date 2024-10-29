# Lets understand file handling.

# Reading a file.
f = open("sample.txt" , 'r')
text = f.read() # Used to read the content
print(text)
f.close()

# Writing to a file.
f = open("sample.txt" , 'w')
f.write("This is added line by opening file in write mode.")
f.close()
# When we write using write mode then privious content gets deleted and new content gets added.

# Writing to a file using append mode
f = open("sample.txt" , 'a')
f.write("This line is added using append mode.")
f.close()

# Another way to open file and perform operation.

with open("sample.txt" , 'a') as f: # IN this way we don't need to close the file explicitly.
    f.write("New line added using with keyword")

# seek() and tell() function.
f = open("sample.txt" , 'r')
print(f.tell()) # This tells the starting reading byte.
f.seek(10) # This sets the starting reading byte to 10 
print(f.tell())
data = f.read()
print(data)