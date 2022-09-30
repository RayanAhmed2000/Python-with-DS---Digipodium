'''
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Print Weird if the number is weird. Otherwise, print Not Weird.
'''


n = int(input())

if n%2==0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("Weird")