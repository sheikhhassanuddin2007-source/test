

def  main():
    for i in range(10):
        if  is_odd(i):
            print("ODD")
        else:
            print("EVEN")

def is_odd(num:int):
    remainder= num %2
    return remainder ==1

if __name__ == "__main__":
    main()               
