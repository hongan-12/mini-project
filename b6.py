import random as rd
# print(rd.randint(1,6))

#b2
a= str(rd.randint(1,9))
b= str(rd.randint(1,9))
c= str(rd.randint(1,9))
d= str(rd.randint(1,9))
print(a+b+c+d)

#b3
a=int(input("Nhập độ dài N: "))

mylist= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ab=rd.choices(mylist,k=a)
print(ab)