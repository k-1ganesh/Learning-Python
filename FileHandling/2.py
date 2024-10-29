# Lets Explore few more methods.

# readline() -> This function reads a single line.
# readlines() -> This functioin returns a list of lines.

with open("sample.txt" , 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
    