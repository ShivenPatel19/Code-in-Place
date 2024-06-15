def main():
    print("Enter a sequence of non-decreasing numbers.")
    num_list = []
    while(True):
        num = float(input("Enter num:"))
        num_list.append(num)
        if num < max(num_list):
            print("Thanks for playing!")
            print(f"Sequence length: {len(num_list)-1}")
            return


if __name__ == "__main__":
    main()