# price = 250 
# print(f"The total price is Rs.{price}")

city = "karachi"
print(f"Welcome to {city}")

# x = 4
# y = 6
# print(f"Product of {x + y}")

# age = 18
# if age >= 18:
#     print("Eligible to vote")

# a = int(input("Enter the value= "))
# if a%2 <= 0:
#     print("The number is Even")
# else:
#     print("The number is Odd")


# day = int(input("Enter the number: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("unknown day")


Marks=int(input("Enter your numbers= "))

if Marks <= 40:
    print("Your grade is F")
elif Marks <= 50:
    print("Your grade is E")
elif Marks <= 60:
    print("Your grade is C")
elif Marks <= 70:
    print("Your grade is B")
elif Marks <= 80:
    print("Your grade is A")
elif Marks <= 100:
    print("Your grade is A+")
else:
    print("unknown number")

# number=int(input("Enter your number: "))
# if number%2:
#     print("the number is Even")
# else:
#     print("the number is odd")

units=int(input("Enter your unit= "))
if units <= 100:
    bill = units * 5
    print(f"Your bill is = {bill}Rs")
else:
    bill = units * 10
    print(f"Your bill is = {bill}Rs")