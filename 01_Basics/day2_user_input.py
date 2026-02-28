"""
Day 2 - User Input & Type Casting
Author: Kabir Sawant
Description: This program takes user input and calculates birth year.
"""

# Taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating birth year
current_year = 2026
birth_year = current_year - age

# Output
print("\nHello,", name)
print("You were born in", birth_year)
print("Keep learning Python daily!")