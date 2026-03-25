def doubled_list(numbers:int):
    return [x*2 for x in numbers]




def main():
    numbers=[1,2,3,4,5]
    if numbers !="":
        result=doubled_list(numbers)
        print(result)

    


if __name__ == "__main__":
    main()
