#Design a program for accepting decimal number divisible by 2. 
def stateA(n):
    if len(n) == 0:
        print('String is accepted')
    else:
        if n[0] == '0':
            stateA(n[1:])
        elif n[0] == '1':
            stateB(n[1:])
        else:
            print('String is not accepted')

def stateB(n):
    if len(n) == 0:
        print('String is not accepted')
    else:
        if n[0] == '0':
            stateA(n[1:])
        elif n[0] == '1':
            stateB(n[1:])
        else:
            print('String is not accepted')

n = input("Given a number: ")
n = bin(int(n))[2:] 
stateA(n)
