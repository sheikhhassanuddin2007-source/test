def list_of_elements(list_of_elements):
    print(list_of_elements)


def user_prompt():
    value=[]
    prompt=input("please enter a number")
    while prompt != "":
        value.append(prompt)
        prompt=input("please enter a number")
    return value


def main():
    values=user_prompt()
    list_of_elements(values)

if "__main__" == __name__:
    main()   