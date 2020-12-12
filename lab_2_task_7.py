a = int(input("введите число "))
b = int(input("введите число "))
с = int(input("введите число "))
if a+b>c and c+b>a and c+a>b:
    print("треугольник существует")
    if a==b or a==c:
        print("равнобедренный")
    elif a==b and a==c and b==c:
        print("равносторонний")
    else:
        print("разносторонний")
else:
    print(0)
