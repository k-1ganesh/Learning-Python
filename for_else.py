# We can use else with for and while loop as well
# Else will execute only when for/while loop will execute completly without break

for i in range(5):
    print(i)
else:
    print("For khatam1")

#############################
    
l1 = [1,2,3,4,5]
for i in l1:
    if i%2==0:
        print(i)
else:
    print("for Khatam2")  

################################

l1 = [1,2,3,4,5]
for i in l1:
    if i%2==0:
        print(i)
    else:
        break    
else:
    print("for Khatam3")  

# Summary else will execute iff for either does not contain break or if contains then  it shouldn't get executed