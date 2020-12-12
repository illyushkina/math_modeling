a = int(input("введите число: "))
b = int(input("введите число: "))
c = int(input("введите число: "))
d = b**2-4*a*c
if d<0:
    print("корней нет")
elif d==0:
    x1 = -b/(2*a)
    print(x)
else:
    x1 = (-b + d**(1/2))/(2*a)
    x2 = (-b - d** (1/2))/(2*a)
    print(x1, x2)