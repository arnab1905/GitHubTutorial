import random
print("Hello World..!")

print("Hi! What's your name?")
myname= input()

print("So {} kindly enter a NUMBER between 1 and 20:".format(myname))

try:
    c=int(input()) #Convert Input value to an Integer, else it will conflict in the for loop!
    #int_c=int(c)
    print("Value entered is",int(c))
    a = random.randint(1,20)
    print("Number drawn is ", a)
    if (c == a):
        print("You've won the lucky draw")
    else:
        print("Tough Luck")

except Exception:
    print("Please enter a number only")