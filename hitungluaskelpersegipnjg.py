# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 07:01:07 2021

@author: Niichaannn
"""
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Hitung Persegi Panjang")
    print("1. Luas")
    print("2. Keliling")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    pil = int(input("Masukkan Pilihan = "))
   
    def luas(p,l):
        L = p*l
        return L
 
    def keliling(p,l):
        K = 2*(p+l)
        return K
    
    if pil == 1:
        p = int(input('Masukan Panjang = '))
        l = int(input('Masukan Lebar = '))
        luas(p,l)
        print('Jadi Luas pesergi panjang adalah ',luas(p,l))
        
    elif pil == 2:
        p = int(input('Masukan Panjang = '))
        l = int(input('Masukan Lebar = '))
        keliling(p,l)
        print('Jadi Keliling pesergi panjang adalah ',keliling(p,l))
        
    else:
        print("Pilihan Tidak Tersedia")
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ?")
    if jwb=="t" or jwb=="T":
        break