#câu 11
while True:
 n=int(input("Nhập 1 số nguyên dương"))
 dem=0
 for i in range(1,n+1):
     if n % i == 0:
         dem += 1
 if dem == 2:
        print(n, "Là số nguyên tố")
 else:
        print(n, "Không là số nguyên tố")
 hoi = input("Tiếp không Thím?(c/k):")
 if hoi in "k":
    print("BYE!")
    break
# câu 12
for i in range(1,11):
 for j in range(2,10):
  line="{0}*{1:>2}={2:>2}".format(j,i,i*j)
  print(line,end='\t')
  print()
#câu 13
a=0
while a<0:
    print('*',end='')
    print()
#câu 14
a=0
while a<0:
    b=0
    while b<40:
        if(a+b)%2==0:
            print('*',end='')
            print()
            a+=1
# câu 15
'''a) range(5)

👉 Tương đương range(0, 5, 1)
→ Bắt đầu từ 0, kết thúc trước 5, bước nhảy 1.
✅ Kết quả: [0, 1, 2, 3, 4]


---

(b) range(5, 10)

→ Bắt đầu từ 5, kết thúc trước 10, bước nhảy mặc định là 1.
✅ [5, 6, 7, 8, 9]


---

(c) range(5, 20, 3)

→ Bắt đầu 5, kết thúc trước 20, bước nhảy +3.
✅ [5, 8, 11, 14, 17]


---

(d) range(20, 5, -1)

→ Bắt đầu 20, đếm ngược đến trước 5, bước nhảy -1.
✅ [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]


---

(e) range(20, 5, -3)

→ Bắt đầu 20, đếm ngược, mỗi lần giảm 3, dừng trước 5.
✅ [20, 17, 14, 11, 8]


---

(f) range(10, 5)

→ Bắt đầu 10, kết thúc trước 5, bước nhảy mặc định là +1.
Nhưng vì 10 > 5 và bước dương, nên không chạy được.
✅ Kết quả: [] (rỗng)


---

(g) range(0)

→ Giống range(0, 0, 1)
Không có số nào từ 0 đến trước 0.
✅ []


---

(h) range(10, 101, 10)

→ Bắt đầu 10, kết thúc trước 101, bước nhảy 10.
✅ [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


---

(i) range(10, -1, -1)

→ Bắt đầu 10, đếm ngược, dừng trước -1.
✅ [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


---

(j) range(-3, 4)

→ Bắt đầu -3, kết thúc trước 4, bước nhảy +1.
✅ [-3, -2, -1, 0, 1, 2, 3]


---

(k) range(0, 10, 1)

→ Bắt đầu 0, kết thúc trước 10, bước nhảy +1.
✅ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].'''