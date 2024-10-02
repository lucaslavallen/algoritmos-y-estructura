import os
os.system('cls')


#! factorial 5! = 5 * 4! = N * N-1
def factorialI(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1,numero+1):
        factorial *= i
        return factorial

def factorialR(numero):
    if numero == 0:
        return 1
    else:
       return numero *  factorialR(numero-1)

print(factorialR(5))
# 120


