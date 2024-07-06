import time
s = time.strftime("%H:%M:%S")  

l1 = s.split(':')
s1 = l1[0]
s2 = l1[1]
s3 = l1[2]
hrs = int(s1)
mnt = int(s2)
sec = int(s3)
print(hrs)
if hrs<12:
    print("Good Morning")
elif hrs>=12 and hrs<=17:
    print("good Evening")

else: 
    print("good night")

for i in range(5):
    time.sleep(1)
    print(i)    