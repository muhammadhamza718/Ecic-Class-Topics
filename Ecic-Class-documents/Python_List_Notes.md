**Python Lists — Detailed Notes** 

**1 What is a List in Python?** 

A **list** is a **collection of items** that is: 

**Ordered** 

**Mutable** (can be changed) 

**Allows duplicate values** 

Can store **multiple data types** 

**Example** 

numbers \= \[10, 20, 30, 40\] 

names \= \["Ali", "Sara", "Ahmed"\] 

mixed \= \[1, "Python", 3.5, True\] 

**2 Creating a List** 

my\_list \= \[\] 

my\_list \= \[1, 2, 3\] 

my\_list \= list((4, 5, 6)) 

**3 Indexing in Lists** 

Index starts from **0** 

Negative indexing starts from **\-1** 

fruits \= \["apple", "banana", "mango"\] print(fruits\[0\]) \# appleprint(fruits\[-1\]) \# mango 

**Index Structure** 

apple banana mango 

0 1 2 

\-3 \-2 \-1 

**4 Slicing in Lists**  
**Syntax** 

list\[start : end : step\] 

**Examples** 

nums \= \[10, 20, 30, 40, 50\] 

print(nums\[1:4\]) \# \[20, 30, 40\]print(nums\[:3\]) \# \[10, 20, 30\]print(nums\[::2\]) \# \[10, 30, 50\]print(nums\[::-1\]) \# reverse list 

**5 Modifying List Elements** 

nums \= \[1, 2, 3\] 

nums\[1\] \= 100print(nums) \# \[1, 100, 3\] 

**6 Adding Elements to List** 

**append()** 

nums \= \[1, 2\] 

nums.append(3) 

**insert()** 

nums.insert(1, 50\) 

**extend()** 

nums.extend(\[4, 5, 6\]) 

**7 Removing Elements from List** 

nums \= \[10, 20, 30, 40\] 

nums.remove(20) \# removes value 

nums.pop() \# removes last element 

nums.pop(1) \# removes by indexdel nums\[0\] \# deletes elementnums.clear() \# empties list 

**8 List Functions & Methods** 

Method Description 

len() Length of list 

max() Maximum value 

min() Minimum value 

sum() Sum of elements 

count() Count occurrences  
Method Description 

index() Find index 

sort() Sort list 

reverse() Reverse list 

copy() Copy list 

nums \= \[3, 1, 4\] 

nums.sort()print(nums) 

**Question 1** 

**Take 5 numbers from user in a list.**   
**Check if the first element is greater than the last element.**   
**If yes, print the middle elements using slicing, otherwise print the list in reverse order.** 

✅ **Code** 

nums \= \[\] 

nums.append(int(input("Enter 1st number: "))) nums.append(int(input("Enter 2nd number: "))) nums.append(int(input("Enter 3rd number: "))) nums.append(int(input("Enter 4th number: "))) nums.append(int(input("Enter 5th number: "))) if nums\[0\] \> nums\[-1\]: 

print("Middle elements:", nums\[1:4\])else: 

print("Reversed list:", nums\[::-1\]) 

**Explanation** 

User inputs 5 values using input() 

Stored in a list using append() 

nums\[0\] → first element 

nums\[-1\] → last element  
If first \> last → slicing nums\[1:4\] Else → reverse using \[::-1\] 

**Question 2** 

**Take a list of 4 numbers from user. If the list length is even, then:** 

**• If first element is even → print last two elements • Else → print first two elements** 

✅ **Code (Nested if)** 

nums \= \[\] 

nums.append(int(input("Enter number 1: "))) nums.append(int(input("Enter number 2: "))) nums.append(int(input("Enter number 3: "))) nums.append(int(input("Enter number 4: "))) if len(nums) % 2 \== 0: 

if nums\[0\] % 2 \== 0: 

print("Last two elements:", nums\[2:4\]) else: 

print("First two elements:", nums\[0:2\]) **Explanation** 

len(nums) checks list length 

Outer if checks even length 

Inner if checks first element even or odd Slicing used to print elements 

No loop used 

**Question 3**  
**Take 6 numbers from user.**   
**If middle two elements are equal, print the list except first and last element. Else print only middle two elements.** 

✅ **Code** 

nums \= \[\] 

nums.append(int(input("Enter 1: "))) 

nums.append(int(input("Enter 2: "))) 

nums.append(int(input("Enter 3: "))) 

nums.append(int(input("Enter 4: "))) 

nums.append(int(input("Enter 5: "))) 

nums.append(int(input("Enter 6: "))) 

if nums\[2\] \== nums\[3\]: 

print("List without first & last:", nums\[1:5\])else: print("Middle elements:", nums\[2:4\]) 

**Explanation** 

Middle of 6 elements → index 2 & 3 

Nested logic not needed here 

Slicing removes first and last 

Works without loop 

**Question 4 (Nested If \+ Input \+ Slicing)** ⭐ 

**Take 5 numbers from user.**   
**If first element \> last element:**   
**• If sum of first two elements \> sum of last two → print first half • Else → print second half** 

✅ **Code** 

nums \= \[\] 

nums.append(int(input("Enter number 1: ")))  
nums.append(int(input("Enter number 2: "))) nums.append(int(input("Enter number 3: "))) nums.append(int(input("Enter number 4: "))) nums.append(int(input("Enter number 5: "))) if nums\[0\] \> nums\[-1\]: 

if nums\[0\] \+ nums\[1\] \> nums\[-1\] \+ nums\[-2\]: print("First half:", nums\[0:3\]) else: 

print("Second half:", nums\[2:5\])else: print("Condition not satisfied") 

**Explanation** 

Outer if compares first & last Inner if compares sums 

Slicing used to divide list 

Nested if logic 

∙ 

**Question 5 (Tricky – Exam Level )** 

**Take 4 numbers from user. If list is palindrome, print middle elements.** 

**Else print reversed list.** 

✅ **Code** 

nums \= \[\] 

nums.append(input("Enter 1: ")) nums.append(input("Enter 2: ")) nums.append(input("Enter 3: ")) nums.append(input("Enter 4: ")) if nums \== nums\[::-1\]: 

print("Middle elements:", nums\[1:3\])else: print("Reversed list:", nums\[::-1\])  
**Explanation** 

Palindrome check using slicing nums\[::-1\] reverses list 

Middle elements via slicing No loop used