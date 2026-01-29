**📄 String Processing Programs – Documentation**

**Program 1: Conditional String Manipulation**

Description

This program takes a string as input and performs different operations based on the length and properties of the string.

Input  
	•	A single string from the user.

Processing Logic  
	1\.	If string length \> 5:  
	•	Condition 1:  
If first half of the string equals the reverse of the second half  
➜ Output: "Palindrome Half"  
	•	Condition 2:  
Else if the string is in uppercase  
➜ Output: string with all vowels removed  
	•	Else:  
➜ Swap the first half and second half of the string  
	2\.	Else (length ≤ 5):  
	•	Print the string twice, excluding the first character

**Program 2: Length-Based String Operations**

Description

This program processes a string based on its length and specific character patterns.

Input  
	•	A single string from the user.

Processing Logic  
	1\.	If length \> 6 and \< 12:  
	•	Condition 1:  
If the first and last characters are the same  
➜ Print the string excluding the first and last characters  
	•	Condition 2:  
Else if the string contains spaces  
➜ Print only the first word  
	•	Else:  
➜ Print alternate characters using slicing  
	2\.	Else:  
	•	Print the reverse of the string

**Program 3: Consonant & Digit Based Processing**

Description

This program manipulates a string based on whether it starts with a consonant and ends with a digit.

Input  
	•	A single string from the user.

Processing Logic  
	1\.	If string starts with a consonant:  
	•	If it ends with a digit:  
➜ Reverse only the first half of the string  
	•	Else:  
➜ Reverse only the second half of the string  
	2\.	Else:  
	•	Print the string without spaces

**Program 4: Advanced String Conditions**

Description

This program performs advanced string transformations based on length and symmetry.

Input  
	•	A single string from the user.

Processing Logic  
	1\.	If length \> 8:  
	•	Condition 1:  
If first half \== second half  
➜ Print "Mirror String"  
	•	Condition 2:  
Else if string starts with a vowel  
➜ Print string without first and last character  
	•	Else:  
➜ Reverse the string using slicing  
	2\.	Else:  
	•	Print the string in uppercase

Output  
	•	Message or transformed string based on conditions.  
