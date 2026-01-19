# Sample coding questions 01 week 01
# Name: Yigit Alkoc
# Student id: 101558073

# question 1 defining variables
# creating array with 1 4 7 9
my_array = [1, 4, 7, 9]
print(f"Array: {my_array}")


# question 2 order of operations
# defining vars a b c d
a = 1
b = 2
c = 3
d = 4

# original equation e = a - b ** c // d + a % c
# fully bracketed version
# order is exponent then floor div then mod then sub/add
e = (a - ((b ** c) // d)) + (a % c)
print(f"Result of fully bracketed expression: {e}")


# question 3 formatting
# temperature variable is 32.6
temperature = 32.6

# using format to show 3 decimal places
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))


# question 4 common functions
# asking user for age input
# need to type 22 when running this
userAge = input("Please enter your age: ")

# printing the sentence with the age
print(f"Now showing the shop items filtered by age: {userAge}")