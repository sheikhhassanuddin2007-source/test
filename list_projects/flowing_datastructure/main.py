def add_three_copies(list,data):
    for i in range (3):
        list.append(data)

def main():
    input_data=input("write your list here")
    list=[]


    result=add_three_copies(input_data,list)
    print("list before []:")
    print("list after",result)



if __name__ == "__main__":
    main()
