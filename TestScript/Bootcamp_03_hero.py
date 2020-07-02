# Write a function that computes the volume of a sphere given its radius.

import string

def vol(r):
    print((4/3)*3.14*(r**3)) #33.49333333333333


# vol(2)

#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    print(num in range(low,high+1)
)
    

# ran_check(5,2,7)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    couter= {'UPPER': 0, 'LOWER': 0}
    
    for i in s:
        if i in string.ascii_uppercase:
            couter['UPPER'] +=1
        elif i in string.ascii_lowercase:
            couter['LOWER'] +=1
    
    print(couter)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_list(lst):
    couter= {}

    for i in lst:
        print(i)
        couter[i] =1

    print(couter.keys())

# unique_list([1,1,1,1,2,2,3,3,3,3,4,5]) #  [1, 2, 3, 4, 5]
def palindrome(s):
    r = []
    
    print(s == s[::-1])

palindrome('helleh')


def ispangram(str1, alphabet=string.ascii_lowercase):
    
    counter=0
    for i in alphabet:
        if i in str1.lower():
            counter +=1
    print(counter == 26)

# ispangram("The quick brown fox jumps over the lazy dog")
