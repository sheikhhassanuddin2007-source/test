


ADULT_AGE:float=18

def is_adult(age:float):
    if age>= ADULT_AGE:
        return "True : You are adult"
    else:
        return "False : you are ot adult"
    
def main():
    age=float(input("Enter your age please : "))
    print(is_adult(age))

if __name__ == "__main__":
    main()        