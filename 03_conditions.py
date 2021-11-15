#Shane
#Practice using expressionand conditional statements

#An expression is a problem that must be solved
#5+5 is an "arithmetic" expression
x=5+5

#Funtions/methods must be resolved as expressions as well
answer=input("what is your name?")

#Comparison expressions resolve as Ture/False
print(7>7)
print(7>=7)
print(x==10)

#A conditional statement runs if its condition is True / not False
if answer == "Bob":
    print("Hello, Bob! Welcome back!")
    print("This line also prints if your name is Bob")
elif answer == "Vadim":
    print("Hey! You still owe me money!")
else:
    print("Sorry, I only talk to Bobs")
print("This line isn't inside of the if statement, and prints regardless")

#^ If checks a condition
#^ Elif Checks a condition if the previous conditions were not True, you can have as many Elifs as you want
#^ Else runs if no prior conditionts were True

age=input("What Is your age?")
age=int(age)
if age >= 10:
    print("Here's your trainer license")
elif age == 9:
    print("You have to wait one year")
else:
    print("You are too young to get your trainer license")
