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
    print("Hitung Transaksi Printer")
    print("Pembelian diatas 1,5 juta mendapat Diskon!")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    n = int (input('Masukkan Jumlah Printer = '))
    #hitung harga
    harga = n*660000
    print("Total Harga Printer sebelum diskon adalah Rp.",harga)
    
    if harga>1500000:
        disc = harga * 0.15
    else:
        disc = 0
        
    print("Pembelian mendapat diskon sebesar Rp.",disc)
    #total harga
    totakhir = harga - disc
    print('Total Harga setelah Diskon adalah Rp.',totakhir)
            
    jwb = input("Apakah mau menghitung ulang (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break