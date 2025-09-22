import math
try:
 r=float(input("Mời bạn nhập bán kính hình tròn:"))
 cv=2*math.pi*r
 dt=r**2
 print("Chu vi =",cv)
 print("Diện tích=",dt)
except:
 print("Lỗi rồi!")
 #tính giờ phút giây
 t = int(input("Nhập số giây:"))
 hour = (t // 3600) % 24
 minute = (t % 3600) // 60
 second = (t % 3600) % 60
 print(hour, ":", minute, ":", second)
 #tính điểm trung bình
 print("Chương trình tính điểm trung bình")
 toan, ly, hoa = eval(input("Nhập điểm toán,lý,hóa:"))
 print("Điểm toán=", toan)
 print("Điểm lý=", ly)
 print("Điểm hóa=", hoa)
 dtb = (toan + ly + hoa) / 3
 print("Điểm trung bình=", dtb)
 print("Điểm làm tròn=", round(dtb, 2))