
inches_in_feet:int=12


def main():
    
    feets:float=float(input("Enter the number of feets to know how much inches they are containing: "))
    feet:float=inches_in_feet*feets

    print(f"The inches in {feets}:feets are {feet}")


if __name__ == "__main__":
    main()
