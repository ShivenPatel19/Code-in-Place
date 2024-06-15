
import random

def main():
    print("Khansole Academy")
    first_num = random.randint(10, 99)
    second_num = random.randint(10, 99)
    print(f"What is{first_num} + {second_num}?")
    user_input = int(input("Your answer:"))
    if user_input == (first_num+second_num):
        print("Correct!")
    else:
        print("Incrrect.")
    
if __name__ == '__main__':
    main()
