# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 06:45:14 2021

@author: Niichaannn
"""

import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Hitung Persegi")
    print("1. Luas")
    print("2. Keliling")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    pil = int(input("Masukkan Pilihan = "))
   
    def luas(s):
        L = s*s
        return L
 
    def keliling(s):
        K = s*4
        return K
    
    if pil == 1:
        s = int(input('Masukan Sisi = '))
        luas(s)
        print('Jadi Luas pesergi adalah ',luas(s))
        
    elif pil == 2:
        s = int(input('Masukan Sisi: '))
        keliling(s)
        print('Jadi Keliling pesergi adalah ',keliling(s))
        
    else:
        print("Pilihan Tidak Tersedia")
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ?")
    if jwb=="t" or jwb=="T":
        break