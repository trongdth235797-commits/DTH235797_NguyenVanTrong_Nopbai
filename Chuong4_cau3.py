def BMI(height, weight):
    return weight / (height ** 2)

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "Obesity class I"
    elif 35 <= bmi <= 39.9:
        return "Obesity class II"
    else:
        return "Obesity class III"

def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <= 24.9:
        return "Trung bình"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Nguy hiểm"

# Chương trình chính
height = float(input("Nhập chiều cao (mét): "))
weight = float(input("Nhập cân nặng (kg): "))
bmi = BMI(height, weight)

print("Chỉ số BMI của bạn là:", round(bmi, 2))
print("Phân loại:", PhanLoai(bmi))
print("Nguy cơ mắc các bệnh liên quan đến béo phì:", NguyCoBenh(bmi))
1.54