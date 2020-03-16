def Basic():
    st = 'Print only the words that start with s in this sentence'

    for i in st.split():
        if i[0] == 's': print(i)

    print(list(range(0, 11, 2)))
    # [0, 2, 4, 6, 8, 10]

    # Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
    x = [i for i in range(1, 51) if i % 3 == 0]
    print(x)

    # Go through the string below and if the length of a word is even print "even!"

    st = 'Print every word in this sentence that has an even number of letters'

    for i in st.split():
        if len(i) % 2 == 0:
            print("even")
        else:
            print("odd")

    # Use List Comprehension to create a list of the first letters of every word in the string below:
    st = 'Create a list of the first letters of every word in this string'
    mylist = [x[0] for x in st.split()]
    print(mylist)


'''
    Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
    instead of the number, and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz".
'''


def FizzBuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def myfunc(word):
    print("".join([i[1].lower() if i[0] % 2 == 0 else i[1].upper() for i in enumerate(word)]))


# Basic()
# FizzBuzz()
# myfunc('ahgdsfhsdfhsdfhskdfhkdf')

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd¶
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


# print(lesser_of_two_evens(2,4))
# print(lesser_of_two_evens(2,5))
# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    (a, b) = text.split(" ")
    return a[0] == b[0]


# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(a, b):
    return a + b == 20 or a == 20 or b == 20


# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(text):
    print(text[:3].capitalize() + text[3:].capitalize())


# old_macdonald('macdonald') 

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    # print(" ".join(text.split(" ")[::-1])) # works too
    print(" ".join(list(reversed(text.split(" ")))))


# master_yoda('I am home') # 'home am I'
# master_yoda('We are ready') #'ready are We'

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    print(abs(100 - n) <= 10 or abs(200 - n) <= 10)


'''
almost_there(104)
almost_there(150)
almost_there(209)
'''


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            print(True)
            return
    print(False)
    return


"""
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
"""


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    x = ''
    for i in text:
        i *= 3
        x += i
    print(x)


"""
paper_doll('Hello')
paper_doll('Mississippi')
"""


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    sumup = sum([a, b, c])

    if sumup <= 21:
        print(sumup)
    elif 11 in [a, b, c] and (sumup - 10) <= 21:
        print(sumup - 10)
    else:
        print('BUST')


"""
blackjack(5,6,7)


blackjack(9,9,9)
blackjack(9,9,11)
blackjack(11,11,11)
"""


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    flag = True
    sumup = 0
    for i in arr:
        if i == 6:
            flag = False
        elif flag and i != 9:
            sumup += i
        elif i == 9:
            flag = True
    print(sumup)


"""
summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
"""


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for i in nums:
        if len(code) > 0 and i == code[0]:
            code.pop(0)

    print(len(code) == 0)


"""
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,0,2,4,0,5,7,7])
spy_game([1,0,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
"""


def count_primes(num):
    x = 3
    primer = [2]
    if num <= 2:
        return 0
    else:
        while x <= num:
            if is_prime(x):
                primer.append(x)
            x += 1
    print(primer)
    print(len(primer))


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


# count_primes(100)


# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    '}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4]}
    if letter.upper() not in alphabet:
        print('Not dictionary')
        return

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])


# print_big('a')
print_big('G')
