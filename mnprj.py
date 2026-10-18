import random
chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chu_so = "0123456789"
dac_biet = "!@#$%^&*()_+"
print("=" *67)
print("                  TRÌNH TẠO MẬT KHẨU NGẪU NHIÊN             ")
print("="*67)
do_dai = int(input("Nhập độ dài mật khẩu (ví dụ 2): "))
chon_hoa = input(" Bao gồm chữ HOA? (y/n): ").strip().lower()
chon_so = input("Bao gồm chữ SỐ? (y/n): ").strip().lower()
chon_dac_biet = input(" Bao gồm KÝ TỰ ĐẶC BIỆT? (y/n): ").strip().lower()
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
print("-"*36)
print(f"       MẬT KHẨU CỦA BẠN:  {mat_khau}")
print("-"*36)