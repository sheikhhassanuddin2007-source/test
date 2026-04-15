


def in_range(n,low,high):
    if n>= low and n<= high:
        return True
    return False


def main():
    n=int(input("Enter a number: "))
    low=50
    high=100

    print(in_range(n,low,high))

if __name__ == "__main__":
    main()    