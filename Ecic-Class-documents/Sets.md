**Python Sets \- Difficult Practice Questions with Solutions** 

 **Symmetric Difference Without Using Built-in Methods** 

\# Input sets 

set1 \= {1, 2, 3, 4} 

set2 \= {3, 4, 5, 6} 

\# Find symmetric difference manually 

sym\_diff \= (set1 \- set2) | (set2 \- set1) 

print("Symmetric Difference:", sym\_diff) 

**Output:** 

Symmetric Difference: {1, 2, 5, 6} 

 **Count Common Elements Across Multiple Sets** 

sets\_list \= \[{1, 2, 3}, {2, 3, 4}, {0, 2, 3}\] 

\# Start with first set 

common\_elements \= sets\_list\[0\] 

\# Loop through other sets 

for s in sets\_list\[1:\]: 

common\_elements &= s \# intersection with current set 

print("Number of common elements:", len(common\_elements)) 

print("Common elements:", common\_elements) 

**Output:** 

Number of common elements: 2 

Common elements: {2, 3} 

1  
 **Subset and Superset Challenge** 

sets\_list \= \[{1,2}, {1,2,3}, {2,3}, {3}\] 

subsets \= \[\] 

supersets \= \[\] 

for s1 in sets\_list: 

for s2 in sets\_list: 

if s1 \!= s2: 

if s1.issubset(s2): 

subsets.append(s1) 

if s1.issuperset(s2): 

supersets.append(s1) 

\# Remove duplicates 

subsets \= \[set(x) for x in set(tuple(x) for x in subsets)\] supersets \= \[set(x) for x in set(tuple(x) for x in supersets)\] 

print("Subsets:", subsets) 

print("Supersets:", supersets) 

**Output:** 

Subsets: \[{1, 2}, {2, 3}, {3}\] 

Supersets: \[{1, 2, 3}\] 

 **Maximum Unique Elements From Set Union** 

sets\_list \= \[{1,2,3}, {3,4,5}, {1,5,6}\] 

max\_union \= set() 

for i in range(len(sets\_list)): 

for j in range(i+1, len(sets\_list)): 

union\_set \= sets\_list\[i\] | sets\_list\[j\] 

if len(union\_set) \> len(max\_union): 

max\_union \= union\_set 

print("Maximum unique elements from any two sets:", max\_union) **Output:** 

2  
Maximum unique elements from any two sets: {1, 2, 3, 4, 5} 

 **Most Frequent Element Across Multiple Sets** 

sets\_list \= \[{1,2,3}, {3,4,5}, {3,5,6}\] 

\# Flatten all elements and count occurrences in sets freq \= {} 

for s in sets\_list: 

for item in s: 

freq\[item\] \= freq.get(item, 0\) \+ 1 

\# Find element with maximum frequency 

max\_count \= max(freq.values()) 

most\_frequent \= \[k for k,v in freq.items() if v \== max\_count\] print("Most frequent element(s) across sets:", most\_frequent) 

**Output:** 

Most frequent element(s) across sets: \[3\] 

3