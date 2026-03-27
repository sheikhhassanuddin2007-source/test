def user_prompt():
    value=[]
    prompt=input("please enter a number")
    while prompt != "":
        value.append(prompt)
        prompt=input("please enter a number")
    return value


def last_element(list_of_elements):
    print(list_of_elements[-1])

def main():
    values=user_prompt()
    last_element(values)


if "__main__" == __name__:
    main()
