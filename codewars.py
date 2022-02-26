# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
#If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else: 
        return (l + w) * 2


#This code does not execute properly. Try to figure out why.

# def multiply(a, b):
#      a * b

def multiply(a, b):
    return a * b

#Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

def sum_str(a, b):
    first_value = 0
    second_value = 0
    
    if a == '':
        first_value = 0
    else:
        first_value = int(a)
        
    if b == '':
        second_value = 0
    else:
        second_value = int(b)
    
    return str(first_value + second_value)


# We need a function that can transform a number into a string.

# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)


#Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    x = sum(int(i) for i in str(n))
    if x > 9:
       return digital_root(x)
    return x

#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.'

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in sentence:
        if i in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

