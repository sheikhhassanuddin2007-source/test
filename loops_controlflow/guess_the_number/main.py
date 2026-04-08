import random


def main():
    secret_number=random.randint(1,99)
    prompt=int(input("Enter numbers to guess "))

    while prompt != secret_number :
        if prompt < secret_number:
            print("your guess is too low ")
        else:
            print("your guess is too high ")

        prompt=int(input("enter numbers to guess  "))    

    print("your guess is correct")

if __name__ == "__main__":
    main()
