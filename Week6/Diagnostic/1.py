def main():
    # TODO write your solution here
    input_value = float(input("Enter your height in meters:"))
    if 1.6 < input_value < 1.9 :
        print("Correct height to be an astronaut")
    if input_value <= 1.6 :
        print("Below minimum astronaut height")
    if input_value >= 1.9 :
        print("Above maximum astronaut height")


if __name__ == "__main__":
    main()
