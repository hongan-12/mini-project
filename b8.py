ten = "An"
tuoi = 15
chieu_cao = 1.57
dang_di_hoc = True
print("ten =", ten, "->", type(ten))
print("tuoi =", tuoi, "->", type(tuoi))
print("chieu_cao =", chieu_cao, "->", type(chieu_cao))
print("dang_di_hoc =", dang_di_hoc, "->", type(dang_di_hoc))
# 2diem -> sai , vì phải bắt đầu bằng chữ không thể bắt đầu bằng số -> diem2
# ho_ten -> đúng , có thể dùng dấu gạch dưới
# tong tien -> sai , không thể có khoảng trắng -> tong_tien
# class -> sai , là từ khoá python -> class_name
# diemTB -> đúng , chữ hoa được phép dùng 
# so-luong -> sai , dấu - là phép tính trừ -> so_luong
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
so = int(input("Nhap mot so: "))
if so % 2 == 0:
    print("So chan")
else:
    print("So le")

print("a", "b", "c", sep="-")
print("Xin chào!", end="")
print("Tạm biệt!")
print("2025", "10", "25", sep="/")
ten = input("Nhap ten: ")
tuoi = int(input("Nhap tuoi: "))
print(f"Xin chao {ten}! Sang nam ban {tuoi + 1} tuoi.")
# phần mở rộng
dai = float(input("Nhap chieu dai: "))
rong = float(input("Nhap chieu rong: "))
chu_vi = (dai + rong) * 2
dien_tich = dai * rong
print("Chu vi:", chu_vi)
print("Dien tich:", dien_tich)
chuoi = "Python"
print(chuoi[0])
print(chuoi[-1])
print(chuoi[:3])
print(chuoi[::-1])
print(chuoi, chuoi, chuoi, sep="-")
toan = float(input("Nhap diem Toan: "))
van = float(input("Nhap diem Van: "))
print("Ca hai mon >= 5:", toan >= 5 and van >= 5)
print("It nhat mot mon >= 8:", toan >= 8 or van >= 8)
print("Bi diem liet:", not (toan >= 3 and van >= 3))
dtb = (toan + van) / 2
hoc_sinh_gioi = dtb >= 8 and toan >= 6 and van >= 6
print("Hoc sinh gioi:", hoc_sinh_gioi)
ho_ten = input("Nhap ho ten: ")
ho_ten_chuan = ho_ten.strip()
print("Chu hoa:", ho_ten_chuan.upper())
print("Chu thuong:", ho_ten_chuan.lower())
so_ky_tu = len(ho_ten_chuan)
print("So ky tu:", so_ky_tu)
print(f'Ho ten "{ho_ten_chuan.upper()}" co {so_ky_tu} ky tu.')

import string
import random
chu_thuong = string.ascii_lowercase
chu_hoa = string.ascii_uppercase
chu_so = string.digits
dac_biet = "!@#$%&*"
toan_bo = chu_thuong + chu_hoa + chu_so + dac_biet
do_dai = int(input("Nhập độ dài mật khẩu (ví dụ 6): "))
chon_hoa = input(" Bao gồm chữ HOA? (y/n): ").strip().lower()
chon_so = input("Bao gồm chữ SỐ? (y/n): ").strip().lower()
chon_dac_biet = input(" Bao gồm KÝ TỰ ĐẶC BIỆT? (y/n): ").strip().lower()
pwd = [
    random.choice(chu_thuong),
    random.choice(chu_hoa),
    random.choice(chu_so),
    random.choice(dac_biet)
]
kho = chu_thuong
if chon_hoa == 'y':
    kho += chu_hoa
if chon_so == 'y':
    kho += chu_so
if chon_dac_biet == 'y':
    kho += dac_biet
mat_khau = ""
for i in range(do_dai):
    mat_khau += random.choice(kho)
print(f"       MẬT KHẨU CỦA BẠN:  {mat_khau}")
