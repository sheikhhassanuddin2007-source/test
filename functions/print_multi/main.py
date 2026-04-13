


def print_multi(message:str,repeats:int):
    for i in range(repeats):
        print(message)


def main():
    prompt=str(input("What you want to print?  "))
    repeats=int(input("How many times you want to repeat?  "))
    print_multi(prompt,repeats)

if __name__ == "__main__":
    main()            