#Câu 6
def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi",
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ"
    elif n < 10:
        return don_vi[n].capitalize()
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hang_chuc[chuc].capitalize()
        elif dv == 1 and chuc > 1:
            return f"{hang_chuc[chuc]} mốt".capitalize()
        elif dv == 5 and chuc > 0:
            return f"{hang_chuc[chuc]} lăm".capitalize()
        else:
            return f"{hang_chuc[chuc]} {don_vi[dv]}".capitalize()

# Test
print(doc_so(35))  # Ba mươi lăm
print(doc_so(5))   # Năm
n=int(input('Nhap so'))
print(doc_so(n))
# câu7
from datetime import datetime, timedelta

def ngay_ke_tiep(ngay, thang, nam):
    try:
        current_date = datetime(nam, thang, ngay)
        next_day = current_date + timedelta(days=1)
        return next_day.strftime("%d/%m/%Y")
    except ValueError:
        return "Ngày không hợp lệ"

# Test
print(ngay_ke_tiep(21, 9, 2025))  # 22/09/2025
print(ngay_ke_tiep(31, 12, 2024)) # 01/01/2025
#câu 8
a = int(input('nhap a:'))
b = int(input('nhap b:'))
c = str(input('nhap toán tử:'))

def tinh_toan(a, b, toan_tu):

    try:
        if toan_tu == '+':
            return a + b
        elif toan_tu == '-':
            return a - b
        elif toan_tu == '*':
            return a * b
        elif toan_tu == '/':
            if b == 0:
                return "Lỗi: chia cho 0"
            return a / b
        else:
            return "Phép toán không hợp lệ"
    except:
        return "Lỗi tính toán"

# Test
print(tinh_toan(5, 3, '+'))  # 8
print(tinh_toan(10, 2, '/')) # 5.0
print(tinh_toan(a, b, c))

# Cau9
thang=int(input('nhap thang:'))

if thang==1 or thang ==2 or thang ==3:
    print('quy1')
elif thang==4 or thang ==5 or thang ==6:
    print('quy2')
elif thang==7 or thang ==8 or thang ==9:
    print('quy3')
elif thang==10 or thang ==11 or thang ==12:
    print('quy4')
else:
    print('không hợp lệ ')

# Câu 10
x=int(input("Nhập x:"))
n=int(input("Nhập N:"))
s=0
for i in range(1,n+1):
 tu=x**i
 mau=1
 for j in range(1,i+1):
  mau=mau*j
 s=s+(tu/mau)
print("s({0},{1})={2}".format(x,n,s))
