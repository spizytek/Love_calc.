# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nm = name1 + name2
newNm1 = nm.lower()

#Name one entry
T1 = newNm1.count("t")
R1 = newNm1.count("r")
U1 = newNm1.count("u")
E1 = newNm1.count("e")

L1= newNm1.count("l")
O1= newNm1.count("o")
V1= newNm1.count("v")
E1= newNm1.count("e")

#Calc. true
Tr = (T1+R1+U1+E1)
#Calc. love
lv = (L1+O1+V1+E1)
res1 = f"{Tr}{lv }"

res = int(res1)
if((res < 10) or (res > 90)):
    print(f"Your score is {res}, you go together like coke and mentos.")
elif((res >= 40) and (res <=50)):
        print(f"Your score is {res}, you are alright together.")
else:
    print(f"Your score is {res}")