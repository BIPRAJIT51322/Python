a = float(input("Enter the number: "))
b = float(input("Enter the exponent: "))
c = a**b;
if c%1==0:
    print(int(a),"^",int(b),"=",int(c))
else:
    print(a,"^",b,"=",c)    