def user_prompt():
    value=[]
    prompt=input("please enter a number")
    while prompt != "":
        value.append(prompt)
        prompt=input("please enter a number")
    return value

def shorten_the_length(list_of_elements):
    max_length:int=3
    while len(list_of_elements) > max_length:
        popped_value=list_of_elements.pop()
        print(popped_value)

def main():
    values=user_prompt()
    shorten_the_length(values)

if "__main__"  == __name__:
    main()          