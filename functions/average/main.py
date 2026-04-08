

def average(a:float,b:float):
    sum=a+b
    return sum/2


def main():
    average1=average(2,18)
    average2=average(22,28)
    finalaverage=average(average1,average2)

    print(average1)
    print(average2)
    print(finalaverage)


if __name__ == "__main__":
    main()    