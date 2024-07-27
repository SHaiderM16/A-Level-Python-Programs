def Factorial(Val):
    f = 1
    for i in range (Val,1,-1):
        f = f*i
    return f
x = int(input("Enter number whose factorial you would like to find: "))
print(Factorial(x))
