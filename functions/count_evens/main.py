

def count_even(lst):
    count=0
    for num in lst:
        if num % 2 ==0:
            count+=1
        print(count)


def get_list():
    lst=[]
    prompt=input("Enter numbers only:  ")
    while prompt != "":
        lst.append(int(prompt)  )          
        prompt=input(("Enter numbers only:  "))
    return lst


def main():
    list=get_list()
    count_even(list)


if __name__ == "__main__":
    main() 