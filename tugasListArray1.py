# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:54:02 2021

@author: Niichaannn
"""
import os
Clear = lambda : os.system('cls')

jwb = "y"
while jwb=="y" or jwb=="Y": 
    Clear() 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Transaksi Biaya Ekspedisi")
    print("by Hasanah Nisa")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Pilihan Kota :")
    print("A. Surabaya")
    print("B. Bandung")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    kode = ['a', 'b']
    kota = ['Surabaya','Bandung']
    jarak = [169, 452]
    ongkirperkm = [2500, 4000]

    pil = input("Masukkan Kode Kota Tujuan : ")
    #identifikasi pilihan
    if pil == 'a' or pil == 'A':
        idx = 0
    elif pil == 'b'or pil == 'B':
        idx = 1
    else:
        print("Pilihan Salah. Silahkan Masukkan Sesuai Kode!")
        break

    #cetak tampilan layar
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Pilihan Tujuan = ",kota[idx])
    print("Jarak          = ",str(jarak[idx],"Km"))
    print("Ongkir per km  = Rp.",str(ongkirperkm[idx]))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #hitung transksi
    fixjarak = jarak[idx]
    hrgongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * hrgongkirkm

    #tampilkan total ongkir
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Total Biaya     = Rp.",str(totongkir))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    jwb = input("Apakah mau menghitung ulang transaksi (Y/T) ? ")
    if jwb=="t" or jwb=="T":
        break