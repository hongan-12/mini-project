name = input("Họ tên: ")
birth_year = int(input("Năm sinh: "))
age = 2026 - birth_year
print(f"Xin chào {name}, năm nay bạn {age} tuổi.")
tu1 = input("Từ 1: ")
tu2 = input("Từ 2: ")
tu3 = input("Từ 3: ")
print(tu1, tu2, tu3, sep="-")
print("Chúc bạn học tốt Python!!!", end="")

name = input("Họ và tên: ")
name = name.strip().title()
print(f"Tên sau khi chuẩn hóa: '{name}'")
sentence = input("Nhập câu văn: ")
print(f"Tổng số ký tự: {len(sentence)}")
print(f"Viết HOA: {sentence.upper()}")
text = input("Nhập từ hoặc dãy số: ")
reverse_text = text[::-1]
print(f"Chuỗi đảo ngược: {reverse_text}")
if text == reverse_text:
    print(f"Kết quả: '{text}' LÀ chuỗi đối xứng!")
else:
    print(f"Kết quả: '{text}' KHÔNG LÀ chuỗi đối xứng!")
    code = input("Nhập mã sản phẩm: ")
loai = code[0:2]
nam = code[3:7]
ten = code[8:]
print(f"Loại SP: {loai}")
print(f"Năm sản xuất: {nam}")
print(f"Tên sản phẩm: {ten}")
full_name=input()
name=full_name.lower().split()
first_name = name[-1]
last_name = "".join(name[:-1])
email = f"{first_name[0]}.{last_name}@company.com"
print(f"Email công ty: {email}")
title=input()
print("=" * 40)
print("***" + title.center(34) + "***")
print("=" * 40)
text = input()
text = text.strip().lower()
print(f"Chuỗi sạch: {text}")
print(f"Độ dài: {len(text)} ký tự")
print(f"3 ký tự đầu: {text[:3]} | 3 ký tự cuối: {text[-3:]}")
name=input("Tên:").strip().title()
color = input("Màu: ").strip().title()
animal = input("Con vật: ").strip().title()
nickname = color + " " + animal + " " + name[::-1][:3]
print("=" * 40)
print(" THẺ SIÊU HÙNG")
print(f"Họ tên    : {name}")
print(f"Biệt danh : {nickname} ")
print("=" * 40)