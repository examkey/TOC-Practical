#Design a Program for creating machine that accepts the string always ending with 101. 
def stateA(n):
    if len(n) == 0:
        print('String is not accepted')
    else:
        if(n[0] == '0'):
            stateA(n[1:])
        elif (n[0] == '1'):
            stateB(n[1:])

def stateB(n):
    if len(n) == 0:
        print('String is not accepted')
    else:
        if(n[0] == '0'):
            stateC(n[1:])
        elif (n[0] == '1'):
            stateB(n[1:])

def stateC(n):
    if len(n) == 0:
        print('String is not accepted')
    else:
        if(n[0] == '0'):
            stateA(n[1:])
        elif (n[0] == '1'):
            stateD(n[1:])

def stateD(n):
    if len(n) == 0:
        print('String is accepted')
    else:
        if (n[0] == '0'):
            stateA(n[1:])
        elif (n[0] == '1'):
            stateB(n[1:])

n = input("Give a String in Combination of 0&1: ")
stateA(n)
