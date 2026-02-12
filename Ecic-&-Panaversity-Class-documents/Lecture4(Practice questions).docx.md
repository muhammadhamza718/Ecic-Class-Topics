Check whether a number is positive or negative  
num \= int(input("Enter a number: "))  
if num \>= 0:  
    print("Positive")else:  
    print("Negative")  
---

Check whether a number is even or odd  
num \= int(input("Enter a number: "))  
if num % 2 \== 0:  
    print("Even")else:  
    print("Odd")  
---

Check whether a person is eligible to vote  
age \= int(input("Enter your age: "))  
if age \>= 18:  
    print("Eligible to vote")else:  
    print("Not eligible to vote")  
---

Check whether a number is divisible by 3  
num \= int(input("Enter a number: "))  
if num % 3 \== 0:  
    print("Divisible by 3")else:  
    print("Not divisible by 3")  
---

Find the greater number between two numbers  
a \= int(input("Enter first number: "))  
b \= int(input("Enter second number: "))  
if a \> b:  
    print("First number is greater")else:  
    print("Second number is greater")  
---

Check whether a number is zero, positive, or negative  
num \= int(input("Enter a number: "))  
if num \> 0:  
    print("Positive")elif num \< 0:  
    print("Negative")else:  
    print("Zero")  
---

Check whether a student passed or failed  
marks \= int(input("Enter marks: "))  
if marks \>= 40:  
    print("Pass")else:  
    print("Fail")  
---

Check whether a year is a leap year  
year \= int(input("Enter year: "))  
if (year % 4 \== 0 and year % 100 \!= 0\) or (year % 400 \== 0):  
    print("Leap Year")else:  
    print("Not a Leap Year")  
---

Check whether a number is divisible by both 5 and 11  
num \= int(input("Enter a number: "))  
if num % 5 \== 0 and num % 11 \== 0:  
    print("Divisible by both 5 and 11")else:  
    print("Not divisible by both")  
---

Find the smaller number between two numbers  
a \= int(input("Enter first number: "))  
b \= int(input("Enter second number: "))  
if a \< b:  
    print("First number is smaller")else:  
    print("Second number is smaller")  
---

Check whether a character is vowel or consonant  
ch \= input("Enter a character: ").lower()  
if ch in 'aeiou':  
    print("Vowel")else:  
    print("Consonant")  
---

Check whether a number is a multiple of 7  
num \= int(input("Enter a number: "))  
if num % 7 \== 0:  
    print("Multiple of 7")else:  
    print("Not a multiple of 7")  
---

Check whether a number is a two-digit number  
num \= int(input("Enter a number: "))  
if 10 \<= abs(num) \<= 99:  
    print("Two-digit number")else:  
    print("Not a two-digit number")  
---

Check whether temperature is hot or normal  
temp \= float(input("Enter temperature in °C: "))  
if temp \> 30:  
    print("Hot")else:  
    print("Normal")  
---

Electricity bill calculation  
Units ≤ 100 → 5 per unit  
Units \> 100 → 10 per unit  
units \= int(input("Enter units consumed: "))  
if units \<= 100:  
    bill \= units \* 5else:  
    bill \= units \* 10  
print("Total Electricity Bill:", bill)

6. STRING PRACTICE QUESTIONS:

**Question:** Print: *My name is Ali and I am 20 years old.*  
name \= "Ali"  
age \= 20  
print(f"My name is {name} and I am {age} years old.")  
**Question:** Print the sum using f-string.  
a \= 10  
b \= 5  
print(f"The sum of {a} and {b} is {a \+ b}")

**Question:** Print: *The price of the book is 450 rupees.*  
price \= 450  
print(f"The price of the book is {price} rupees.")  
**Question:** Print square of a number using f-string.  
num \= 6  
print(f"The square of {num} is {num\*\*2}")  
**Question:** Print a greeting message with user’s name.  
name \= input("Enter your name: ")  
print(f"Hello {name}, welcome to Python programming\!")  
**Question:** Show total marks and percentage.  
marks \= 420  
total \= 500  
percentage \= (marks / total) \* 100  
print(f"You got {marks} out of {total}. Percentage \= {percentage}%")  
**Question:** Print value up to 2 decimal places.  
value \= 3.14159  
print(f"Value up to 2 decimal places: {value:.2f}")  
**Question:** Print 5 × 3 \= 15 format.  
num \= 5  
print(f"{num} x 3 \= {num \* 3}")  
**Question:** Show pass or fail using f-string.  
marks \= 35  
result \= "Pass"   
if marks \>= 40   
else "Fail"  
print(f"Marks: {marks}, Result: {result}")  
**Question:** Display student details.  
name \= "Ayesha"  
roll \= 23  
marks \= 88  
print(f"Student Name: {name}\\nRoll No: {roll}\\nMarks: {marks}")

**Question:** Find area of a rectangle.  
length \= 10  
width \= 5  
print(f"Area of rectangle is {length \* width}")  
**Question:** Print date in format: 11-01-2026  
day \= 11  
month \= 1  
year \= 2026  
print(f"{day:02d}-{month:02d}-{year}")  
**Question:** Print text in aligned form.  
item \= "Pen"  
price \= 20  
print(f"{item:\<10} | {price:\>5}")

