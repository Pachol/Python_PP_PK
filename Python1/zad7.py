import math

print( "Put parameters:")
a = input("a = ")
b = input("b = ")
c = input("c = ")

a=float(a)
b=float(b)
c=float(c)

delta = b*b - 4*a*c
print("delta :")
print(delta)
if delta > 0:
   x1=((-1)*b+math.pow(delta,0.5))/(2*a)
   print(x1)
   x2=((-1)*b-math.pow(delta,0.5))/(2*a)
   print(x2)
elif delta == 0:
   x = math.pow(2 * a, -1) * (-1) * b
   print(x)
else:
   print("no real roots")
