# việt hàm để tính diện tích tam giac
from math import sqrt
print("Viết chương trình tính diện tich tích tam giác")
a=float(input("Nhâp cạnh a>0:"))
b=float(input("Nhâp cạnh b>0:"))
c=float(input("Nhâp cạnh c>0:"))
if(a<=0 or b<=0 or c<=0)or (a+b<=c)or(a+c<=b)or(b+c<=a):
    print("Cạnh tam giác phải lớn hơn 0")
else:
    cv=a+b+c
    p=(cv)/2
    S=sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác là:",S)