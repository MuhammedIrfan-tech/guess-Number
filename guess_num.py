# python function code for simple guess a number
import random
def guess():
    n=10
    num=random.randint(1,100)
    for i in range(n):
        chance=n-i
        gues=int(input('enter a number'))
        if num==gues:
            print(f'you got the number hurrayy...')
        else:
            print(f'better luck')
        print(f'You have {chance} only....')
guess()
        