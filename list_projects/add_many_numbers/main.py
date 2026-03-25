def total(numbers):
    return sum(numbers)

def main():
    numbers=input("Write your numbers")
    value=[]

    try:
        line=[int(x)for x in numbers]
    except ValueError:
        print("invalid syntax")


    result=total(numbers)      
    print(result)

if __name__ == "__main__":
    main()