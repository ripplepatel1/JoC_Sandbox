# Ripple Patel

import math

# Write a function is_even that takes a number as a parameter
# and returns whether or not it is even. Test that your function
# works by calling it twice, once with an even number and once
# with an odd number, and print the results.

def is_even(num):
    if (num%2 ==1):
        print(num, "is the odd number.")
    else:
        print(num, "is the even number.")

def calculate_total(meal, tax_rate, tip_rate):
    tip = meal * tip_rate
    tax = meal * tax_rate
    return meal + tip + tax

def hey(num):
    return(num * num)

def there(n):
    if n >=0:
        return 2 ** n
    else:
        return 0

def are_we(num, string):
    for i in range (num):
        print("Are we", string, "yet?", end=" ")
        print()
def main():
    is_even(8)
    is_even(7)
    print("Total meal is: $", calculate_total(53.48, .07,.18))
    print(hey(5))
    print(hey(0))
    print(hey(-3))
    print()
    print(there(5))
    print(there(0))
    print(there(3))
    print(there(-2))
    print(there(-6))
    print()
    are_we (4, "there")
    are_we (3, "50")
    are_we (1, "")
    are_we (0, "hey")
main()




