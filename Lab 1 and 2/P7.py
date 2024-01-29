#Python program to solve quadratioc equation
import math
print("In the equation ax^2 +bx +c")
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))

d=math.sqrt((b*b)-(4*a*c))

s1=(-b+d)/(2*a)
s2=(-b-d)/(2*a)

print("Solution 1 is %0.2f"%s1)
print("Solution 2 is %0.2f"%s2)
