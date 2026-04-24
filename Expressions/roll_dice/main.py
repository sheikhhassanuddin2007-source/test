
import random

num_dice:int=6

def main():
    die1:int=random.randint(1,num_dice)
    die2:int=random.randint(1,num_dice)

    total=die1+die2


    print(f"The starting of the dice is: {num_dice}")
    print(f"The die1 is:{die1}")
    print(f"The die2 is:{die2}")
    print(f"The total of the two dices is :{total}")
    


if __name__ == "__main__":
    main()
