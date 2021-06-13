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
    print("Hitung Transaksi Printer")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    n = int (input('Masukkan Jumlah Printer = '))
    #hitung harga
    harga = n*660000
    print("Total Harga Printer adalah",harga)
        
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break