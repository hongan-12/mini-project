dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
chu_vi = (dai + rong) * 2
dien_tich = dai * rong
print("Chu vi:", chu_vi)
print("Diện tích:", dien_tich)
phut = int(input("Nhập số phút: "))
gio = phut // 60
phut_le = phut % 60
print(gio, "giờ", phut_le, "phút")