# Câu 1
print("Chương trình kiểm tra năm nhuần")
year=int(input("Mời Thím nhập vào 1 năm:"))
if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
 print("Năm ", year, " là năm nhuần")
else:
 print("Năm ", year, " không nhuần")
 # câu 2
 print("Chương trình đếm số ngày trong tháng")
 month = int(input("Nhập vào 1 tháng:"))
 if month in (1, 3, 5, 7, 8, 10, 12):
     print("Tháng ", month, " có 31 ngày")
 elif month in (4, 6, 9, 11):
     print("Tháng ", month, " có 30 ngày")
 elif month == 2:
    year = int(input("Mời bạn nhập vào năm:"))
    if (year % 4 == 0 and year % 100 != 0 or year % 400
 == 0):
        print("Tháng ", month, " có 29 ngày")
    else:
     print("Tháng ", month, " có 28 ngày")
 else:
  print("Tháng ", month, " không hợp lệ")
#Câu3
from math import sqrt
print("Chương trình Giải Phương trình bậc 2")
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
if a == 0:
 #bx+c=0
 if b == 0 and c ==0:
  print("Vô số nghiệm")
 elif b==0 and c !=0:
  print("Vô nghiệm")
 else:
     x = -c / b
     print("No x=", x)
else:
 delta = b ** 2 - 4 * a * c
 if delta < 0:
     print("Vô No")
 elif delta == 0:
    x = -b / (2 * a)
    print("No kép x1=x2=", x)
 else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print("x1=", x1)
    print("x2=", x2)
# câu 4
'''Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
(a) x == 3
(b) x < y
(c) x >= y
(d) x <= y
(e) x != y - 2
(f) x < 10
(g) x >= 0 and x < 10
(h) x < 0 and x < 10
(i) x >= 0 and x < 2
(j) x < 0 or x < 10
(k) x > 0 or x < 10
(l) x < 0 or x > 10'''

x,y,z = 3,5,7
if x==3:
      print('true')
if x<y:
      print('true')
else :
      print('false')
if x>=y:
      print('true')
else :
      print('false')
if x<=y:
      print('true')
else :
      print('false')
if x!=y-2:
      print('true')
else :
      print('false')
if x<10:
      print('true')
else :
      print('false')
if x>=10 and x<10:
    print('true')
else:
    print('false')
if x>0 and x<20:
    print('true')
else:
    print('false')
if x<0 or x<10:
    print('true')
else :
    print('false')
if x>0 or x<10:
    print('true')
else :
    print('false')
if x<0 or x>10:
    print('true')
else:
    print('false')
# câu 5
i =int(input("nhap i"))
j=int(input("nhap j"))
k=int(input("nhap k"))
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
     if j>k:
        j=i
     else:
       i=k
print("i=",i,",j=",j,",k=",k)
