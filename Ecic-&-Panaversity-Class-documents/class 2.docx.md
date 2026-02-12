## **Python Indentation**

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

if 5 \> 2:  
  print("Five is greater than two\!")

## **Many Statements**

Most Python programs contain many statements.

The statements are executed one by one, in the same order as they are written:

### **Example**

print("Hello World\!")  
print("Have a good day.")  
print("Learning Python is fun\!")

## **Semicolons (Optional, Rarely Used)**

Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:

### **Example**

print("Hello"); print("How are you?"); print("Bye bye\!")

You can use the [print()](https://www.w3schools.com/python/ref_func_print.asp) function as many times as you want. Each call prints text on a new line by default:

### **Example**

print("Hello World\!")  
print("I am learning Python.")  
print("It is awesome\!")

Agr yaha mai numbers likh do tb bhi ye aise hi print hoge same jaise in wording mai print horhe

You can also do math inside the [print()](https://www.w3schools.com/python/ref_func_print.asp) function:

### **Example**

print(3 + 3)  
print(2 \* 5)

## **Double Quotes**

Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

### **Example**

print("This will work\!")  
print('This will also work\!')

## **Print Without a New Line**

By default, the [print()](https://www.w3schools.com/python/ref_func_print.asp) function ends with a new line.

If you want to print multiple words on the same line, you can use the end parameter:

### **Example**

print("Hello World\!", end=" ")  
print("end use for print multipe word on same line ")

## **Mix Text and Numbers**

You can combine text and numbers in one output by separating them with a comma:

### **Example**

print("My name is Qirrat" ,"I am",23,"years old.")

# **Python Comments**

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

\#This is a comment  
print("Hello, World\!")

print("Hello, World\!") \#This is a comment

## **Variables**

### **Newline confusion**

print("Hello\\nWorld")

Variables are containers for storing data values.

## **Creating Variables**

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

x \= 4       \# x is of type int  
x \= "Sally" \# x is now of type str  
print(x)

## **Casting**

If you want to specify the data type of a variable, this can be done with casting.

### **Example**

x \= str(3)    \# x will be '3'  
y \= int(3)    \# y will be 3  
z \= float(3)  \# z will be 3\.

## **Get the Type**

You can get the data type of a variable with the [type()](https://www.w3schools.com/python/ref_func_type.asp) function.

### **Example**

a \= 50  
b \= "qirrat"  
print(type(a))  
print(type(b))

## **Single or Double Quotes?**

String variables can be declared either by using single or double quotes:

### **Example**

x \= "John"  
\# is the same as  
x \= 'John'

## **Case-Sensitive**

Variable names are case-sensitive.

### **Example**

This will create two variables:

a \= 4  
A \= "Sally"  
\#A will not overwrite a

## **Variable Names**

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total\_volume).

Rules for Python variables:

* A variable name must start with a letter or the underscore character  
* A variable name cannot start with a number  
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )  
* Variable names are case-sensitive (age, Age and AGE are three different variables)  
* A variable name cannot be any of the [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp).

### **Example[Get your own Python Server](https://www.w3schools.com/python/python_server.asp)**

Legal variable names:

myvar \= "John"  
my\_var \= "John"  
\_my\_var \= "John"  
myVar \= "John"  
MYVAR \= "John"  
myvar2 \= "John"

### **Example**

Illegal variable names:

2myvar \= "John"  
my-var \= "John"  
my var \= "John"

## **Many Values to Multiple Variables**

Python allows you to assign values to multiple variables in one line:

### **Example[Get your own Python Server](https://www.w3schools.com/python/python_server.asp)**

x, y, z \= "Orange", "Banana", "Cherry"  
print(x)  
print(y)  
print(z)

## **One Value to Multiple Variables**

And you can assign the same value to multiple variables in one line:

### **Example**

x \= y \= z \= "Orange"  
print(x)  
print(y)  
print(z)

## **Unpack a Collection**

If you have a collection of values in a [list](https://www.w3schools.com/python/python_lists.asp), [tuple](https://www.w3schools.com/python/python_tuples.asp) etc. Python allows you to extract the values into variables. This is called unpacking.

### **Example**

Unpack a list:

fruits \= \["apple", "banana", "cherry"\]  
x, y, z \= fruits  
print(x)  
print(y)  
print(z)

## **Output Variables**

The [print()](https://www.w3schools.com/python/ref_func_print.asp) function is often used to output variables.

### **Example[Get your own Python Server](https://www.w3schools.com/python/python_server.asp)**

x \= "Python is awesome"  
print(x)

In the [print()](https://www.w3schools.com/python/ref_func_print.asp) function, you output multiple variables, separated by a comma:

### **Example**

x \= "Python"  
y \= "is"  
z \= "awesome"  
print(x, y, z)

Agr , kii jagah \+ ajaye tb bhi ye aik hi line mai print hoga like python is awesome 

For numbers, the \+ character works as a mathematical operator:

### **Example**

x \= 5  
y \= 10  
print(x \+ y)

In the [print()](https://www.w3schools.com/python/ref_func_print.asp) function, when you try to combine a string and a number with the \+ operator, Python will give you an error:

### **Example**

x \= 5  
y \= "John"  
print(x \+ y)

The best way to output multiple variables in the [print()](https://www.w3schools.com/python/ref_func_print.asp) function is to separate them with commas, which even support different data types:

### **Example**

x \= 5  
y \= "John"  
print(x, y)

## **Storing a Number**

#### **a) Integer Input**

age \= int(input("Enter your age: "))print(age)

#### **b) Float Input**

salary \= float(input("Enter your salary: "))print(salary)

age \= 20print(age)  
✔ age is a variable  
✔ 20 is the value stored in it

### **Taking Multiple Inputs**

You can take multiple inputs in one program.  
name \= input("Enter name: ")  
age \= int(input("Enter age: "))print(name, age)

---

## **2️⃣ Storing a Decimal Value**

price \= 99.5print(price)  
---

## **3️⃣ Storing Text (String)**

name \= "Ali"print(name)  
---

## **4️⃣ Storing True / False (Boolean)**

is\_student \= Trueprint(is\_student)  
---

## **5️⃣ Multiple Variables**

name \= "Sara"  
age \= 22  
marks \= 85.5  
print(name)print(age)print(marks)  
---

## **6️⃣ Printing Variables Together**

name \= "Ahmed"  
age \= 21  
print("Name:", name)print("Age:", age)  
---

## **7️⃣ Changing Variable Value**

x \= 10print(x)

x \= 20print(x)  
📌 Python allows changing values easily.  
---

## **8️⃣ Simple Calculation Using Variables**

a \= 5  
b \= 3  
sum \= a \+ b  
print(sum)  
---

## **9️⃣ Taking Input from User**

name \= input("Enter your name: ")  
print("Hello", name)

