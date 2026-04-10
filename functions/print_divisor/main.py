


def divisor(num:int):
    print("The divider of :  ",num)
    for i in range(num):
        cur_divisor=i+1
        if num % cur_divisor ==0:
            print(cur_divisor)


def main():
    prompt=int(input("Enter numbers only:  "))
    divisor(prompt)


if __name__ == "__main__":
    main()                