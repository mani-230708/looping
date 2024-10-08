'''
a = 0, b=0, c=1 are the 1st three terms. All other terms in the Lucas sequence are generated by the sum of their 3 most recent predecessors. Write a program to generate the first n terms of a Lucas Sequence.
Input format:
The input containing an integer 'n' which denotes the given number
Output format:
Print the  'n' terms of the Lucas Sequence, separated by a single space. There are no leading or trailing spaces in the output.
Refer the sample output for formatting.
Sample Input:
5
Sample Output:
0 0 1 1 2

n=int(input())
a=0
b=0
c=1
print(a,end=’ ‘)
print(b,end=’ ‘)
print(c,end=’ ‘)
for i in range (4,n+1):
	d=a+b+c
	a=b
	b=c
	c=d
	print(d,end=’ ‘)
# Read the input integer
n = int(input())

# Initialize the first three terms
a = 0
b = 0
c = 1

# Create a list to hold the sequence
lucas_sequence = []

# Generate the Lucas sequence
for i in range(n):
    if i == 0:
        lucas_sequence.append(a)
    elif i == 1:
        lucas_sequence.append(b)
    elif i == 2:
        lucas_sequence.append(c)
    else:
        d = a + b + c  # Calculate the next term
        lucas_sequence.append(d)
        a, b, c = b, c, d  # Update the three most recent predecessors

# Print the terms in the sequence separated by a space
print(" ".join(map(str, lucas_sequence)))
'''
