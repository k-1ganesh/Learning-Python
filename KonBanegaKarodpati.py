print("Welcome to the game")
print("Each question has Reward and Reward is increasing with repect to the level of difficulty")
print("SO are you ready ? ")
a = input("Enter Yes or No: ")
if a=="No":
    print("Alright")
else:
    Reward = 0
    Exam = [("What is 35*10" , "350"),("Who is prime minister of India ?","Narendra Modi"),("Sqaure of 35?","1225")]
    for i in Exam:
        print(i[0])
        ans = input()
        if ans==i[1]:
            Reward = Reward + 100

    if Reward==0:
        print("Sorry ! Better luck next time")
    else:
        print("You have earned ",Reward," Money")






