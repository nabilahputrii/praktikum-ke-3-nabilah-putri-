# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:48:17 2021

@judul : praktikum 3
@NIM : 065002100002
@Nama : Nabilah Putri
"""

print("hallo semua, nama saya nabilah putri")
print("hari ini kita akan menentukan segitiga")
a = float(input("silahkan anda masukan panjang sisi A:"))
b = float(input("silahkan anda masukan panjang sisi B:"))
c = float(input("silahkan anda masukan panjang sisi C:"))


if(a == b == c):
    print("ini adalah segitiga sama sisi")
elif(a==b or b==c or c==a):
    print("ini adalah segitiga sama kaki")
elif((a + b <= c) or (a + c <= b) or (b + c <= a)):
    print(" ini bukan segitiga")
elif (a + b >=c) or (a + c >=b) or (b + c >=a):
    print("ini adalah segitiga sama kaki")
else:
    print("adalah segitiga sembarang")
    

