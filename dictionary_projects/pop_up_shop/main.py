

def main():
    fruits={"apple":1,"banana":2,"cherry":5}
    total_cost=0

    for fruite_name,price in fruits.items():
        while True:
            prompt=input(f"Please  tell how many {fruite_name} you want to buy")
            if prompt == "":
                print("please enter a number cannot be empty")
                continue
            try:
                amount_bought=int(prompt)
                if amount_bought <0:
                    print("please enter positive numners")
                    continue
                break
            except ValueError:
                print("please enter whole numbers ")
        total_cost +=price*amount_bought
    print(f"Your total cost $ is {total_cost}")


if "__main__" == __name__:
    main()               