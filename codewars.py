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