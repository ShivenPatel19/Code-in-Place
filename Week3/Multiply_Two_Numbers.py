"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    # your code here
    n=int(input("Enter first number:"))
    m=int(input("Enter second number:"))
    result=n*m
    print(result)
    


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
