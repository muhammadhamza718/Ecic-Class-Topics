## **Today Topics :**

12-jan-2026

## **1\. f-string (Formatted String) in Python**

### **Definition**

An **f-string** is used to insert variables or expressions directly inside a string using {}.

### **Syntax**

f"string {variable}"

### **Example**

name \= "Ali"  
age \= 20  
print(f"My name is {name} and I am {age} years old")

### **Features**

Introduced in **Python 3.6**  
Faster and more readable than other formatting methods  
Can include expressions

### **Example with expression:**

a \= 5  
b \= 3  
print(f"Sum is {a \+ b}")  
---

## **2\. if, else, elif Conditional Statements**

### **Definition**

Conditional statements are used to **make decisions** based on conditions.  
---

### **if Statement**

Executes a block of code if the condition is **True**.  
age \= 18if age \>= 18:  
    print("Eligible to vote")  
---

### **else Statement**

Executes when the if condition is **False**.  
age \= 16if age \>= 18:  
    print("Eligible")else:  
    print("Not eligible")  
---

### **elif Statement**

Used to check **multiple conditions**.  
marks \= 75  
if marks \>= 90:  
    print("Grade A")elif marks \>= 70:  
    print("Grade B")else:  
    print("Grade C")

### **Important Points**

if is mandatory  
elif and else are optional  
Indentation is required  
---

## **3\. Indexing in Python**

### **Definition**

Indexing is used to **access individual elements** of a sequence (string, list, tuple).

### **Index starts from 0**

### **Example (String Indexing)**

text \= "Python"  
print(text\[0\])   \# Pprint(text\[3\])   \# h  
---

### **Negative Indexing**

Access elements from the **end**.  
print(text\[-1\])  \# nprint(text\[-2\])  \# o  
---

## **4\. Slicing in Python**

### **Definition**

Slicing is used to **extract a part** of a sequence.

### **Syntax**

sequence\[start : end : step\]  
start → starting index (included)  
end → ending index (excluded)  
step → jump value (optional)  
---

### **Examples**

text \= "Python Programming"  
print(text\[0:6\])      \# Pythonprint(text\[7:18\])       
print(text\[:6\])       \# Python  
print(text\[7:\])       \# Programming  
---

### **Slicing with Step**

print(text\[::2\])      \# Pto rgamn  
---

### **Reverse String using Slicing**

print(text\[::-1\])  
---

## **Quick Summary Table**

| Topic | Purpose |
| ----- | ----- |
| f-string | Insert variables in strings |
| if | Check condition |
| elif | Multiple conditions |
| else | Default condition |
| Indexing | Access single element |
| Slicing | Access multiple elements |

## **🔹 Practice Questions: f-String**

### **Q1:**

Create two variable name and age.  
Use an **f-string** to print:  
My name is \_\_\_ and I am \_\_\_ years old.  
---

### **Q2:**

Create two numbers a \= 10 and b \= 5.  
Use an f-string to print their **sum**.  
---

### **Q3:**

Create a variable price \= 250.  
Use an f-string to print:  
The total price is Rs.250  
---

### **Q4:**

Take a variable city and print:  
Welcome to {city}  
(using f-string)  
---

### **Q5:**

Create variables x \= 4, y \= 6.  
Use an f-string to print the **product** of x and y.  
---

## **🔹 Practice Questions: Slicing & Indexing**

### **Q6**

Given:  
text \= "PythonProgramming"  
Print:

* First character  
* Last character  
* The word **Python** using slicing

---

### **Q7:Using the same string, print Programming using slicing.**

---

### **Q8:Print every second character from the string using slicing.**

---

### **Q9:Reverse the string using slicing.**

---

---

## **🔹 Practice Questions: if–else (Basic)**

### **Q11:Write a program to check whether a number is positive or negative.**

---

### **Q12:Write a program to check whether a number is even or odd.**

---

### **Q13:Write a program to check whether a person is eligible to vote (age ≥ 18).**

---

### **Q14:Write a program to check whether a number is greater than 50 or not.**

---

### **Q15:Take marks as input and print:**

**Pass** if marks ≥ 40  
**Fail** otherwise  
---

