


def sentence_maker(word:str,part_of_speech:int):

    if part_of_speech == 0:
        print(f"The wheels on the bus go round"  + word + "round")

    elif part_of_speech == 1:
        print(f"The horn on the bus go " +  word + "beep beep") 

    elif part_of_speech == 2:
        print(f"The driver on the bus go how are " + word)

    else:
        print("The poem should be in string  ") 


def main():
    word=str(input("Which sentence you want to complete write a word to comple a tense:  "))
    print("Is this for 0 or 1 or 2  ") 
    part_of_speech=int(input("PLease enter 0 or 1 or 2:  "))
    sentence_maker(word,part_of_speech)

if __name__ == "__main__":
    main()

