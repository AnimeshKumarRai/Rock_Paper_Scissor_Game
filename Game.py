import random


def game(comp,you):
    if comp==you:
        return 2
    elif comp=="r":
        if you=="s":
            return 0
        elif you=="p":
            return 1
    elif comp=="p":
        if you=="r":
            return 0
        elif you=="s":
            return 1
    elif comp=="s":
        if you=="p":
            return 0
        elif you=="r":
            return 1
    else:
        print("Worng Choice")

print("Computer turn : Rock(r),Paper(p) or Scissor(s)")
randno=random.randint(1,3)
if randno==1:
    comp="r"
elif randno==2:
    comp="p"
elif randno==3:
    comp="s"

you=input("Your Turn : Rock(r),Paper(p) or Scissor(s) : ")
a=game(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a==2:
    print("Match is tie")
elif a==1:
    print("You Win")
else:
    print("You Loose")
