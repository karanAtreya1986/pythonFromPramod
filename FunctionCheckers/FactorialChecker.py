numb=int(input("Enter number"))
#fact =1
def checkFactorial(numb):
    fact = 1
    for i in range(1, numb+1):
        fact=fact*i
    return fact

result=checkFactorial(numb)
print(result)
