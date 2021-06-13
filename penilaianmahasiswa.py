# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 08:01:05 2021

@author: Niichaannn
"""
#Penilaian Mahasiswa
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Penilaian Mahasiswa")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    n = int(input("Masukkan Nilai = "))
    #cek nilai
    if int(n)>0 and int(n)<=100:
        if n>=91:
            sts = "A"
        elif n>=81: sts="B"
        elif n>=71: sts="C"
        else:
            sts = "D"
        print(sts)
    else:
        pesan="Masukkan 0-100 saja"
        print(pesan)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break
