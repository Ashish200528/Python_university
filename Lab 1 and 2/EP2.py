#To read the coefficients

#y=ax^2+bx+c
print("In the equation ax^2+ bx + c ")
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
x=int(input("Enter the value of x "))
print(f"The answer of expression is {(a*x*x)+(b*x)+c}")

#a=(b+c)*(b-c)
print("In the equation a=(b+c)*(b-c) ")
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
print(f"The answer of expression is {(b+c)*(b-c)}")

#A=-(R1/R2+R3)
print("In the equation A=-(R1/R2+R3)")
R1=int(input("Enter the value of R1 "))
R2=int(input("Enter the value of R2 "))
R3=int(input("Enter the value of R3 "))
print(f"The answer of expression is {-((R1/R2)+R3)}")

#I=(P*R*T)/100
print("In the equation I=(P*R*T)/100")
P=int(input("Enter the value of P "))
R=int(input("Enter the value of R "))
T=int(input("Enter the value of T "))
print(f"The answer of expression is {(P*R*T)/100}")
