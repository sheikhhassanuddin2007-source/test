


def main():
    dividend:float=float(input("Enter a number to be divided: "))
    divisor:float=float(input("Enter a number to divide bt: "))


    cotient=(dividend//divisor)
    remainder=(dividend%divisor)

    print(f"The result is {cotient} and the remainder is {remainder}")



if __name__ == "__main__":
    main()
