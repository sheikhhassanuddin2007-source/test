


import random 

DONELIKELIHOOD=0.3

def chaotic_counting():
    for i in range(10):
        cur_num=i+1
        if done():
            return
        print(cur_num)

def done():
    if random.random() <DONELIKELIHOOD:
        return True
    return False

def main():
    print("Im counting to 10 or which comes first")
    chaotic_counting()
    print("Im done")        

if __name__  == "__main__":
    main()    