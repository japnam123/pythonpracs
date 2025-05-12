import math
import random
import calendar
from datetime import datetime

def calculate_circle_area():
    """Calculate area of a circle based on radius"""
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"r = {radius}")
    print(f"Area = {area}")

def reverse_name():
    """Reverse first and last name"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"{last_name} {first_name}")

def create_list_tuple():
    """Create list and tuple from comma-separated numbers"""
    numbers = input("Enter comma-separated numbers: ")
    num_list = numbers.split(',')
    num_tuple = tuple(num_list)
    print(f"List: {num_list}")
    print(f"Tuple: {num_tuple}")

def check_even_odd():
    """Check if a number is even or odd"""
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def concatenate_strings():
    """Concatenate N strings"""
    n = int(input("Enter number of strings: "))
    strings = []
    for i in range(n):
        string = input(f"Enter string {i+1}: ")
        strings.append(string)
    result = ''.join(strings)
    print(f"Concatenated string: {result}")

def arithmetic_operations():
    """Perform addition and division"""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Addition: {num1 + num2}")
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Cannot divide by zero")

def calculate_triangle_area():
    """Calculate area of a triangle"""
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print(f"Area of triangle: {area}")

def swap_variables():
    """Swap two variables"""
    a = input("Enter first variable: ")
    b = input("Enter second variable: ")
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def generate_random_number():
    """Generate a random number"""
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))
    random_num = random.randint(start, end)
    print(f"Random number: {random_num}")

def km_to_miles():
    """Convert kilometers to miles"""
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers = {miles} miles")

def display_calendar():
    """Display calendar"""
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))

def swap_without_temp():
    """Swap two variables without temporary variable"""
    a = input("Enter first variable: ")
    b = input("Enter second variable: ")
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")

def check_number_sign():
    """Check if number is positive, negative or zero"""
    number = float(input("Enter a number: "))
    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

def check_leap_year():
    """Check if a year is leap year"""
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

if __name__ == "__main__":
    # Example usage
    calculate_circle_area()
    reverse_name()
    create_list_tuple()
    check_even_odd()
    concatenate_strings()
    arithmetic_operations()
    calculate_triangle_area()
    swap_variables()
    generate_random_number()
    km_to_miles()
    display_calendar()
    swap_without_temp()
    check_number_sign()
    check_leap_year() 