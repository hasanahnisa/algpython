# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 12:09:56 2021

@author: Niichaannn
"""

#tanggal
import datetime
import os

jwb ="y"
while jwb =="y" or "Y":
    os.system('cls')
    #input 
    print("")
    print("===================================")
    print("Perhitungan Gaji Karyawan")
    print("===================================")
    nama = input("Masukkan Nama :")
    gol = input("Masukkan Golongan : ")
    jns_klmn = input("Masukkan Jenis Kelamin (Laki-laki/Perempuan): ")
    jns_klmn = jns_klmn.lower()
    sts_kwn = input("Masukkan Status Kawin (Kawin/Belum) : ")
    sts_kwn = sts_kwn.lower()
    anak = input("Apakah Punya Anak (Y/T) ? ")
        
    kode = ['1','2','3']
    pokok = [2500000,4500000,6500000]  
     
    #golongan
    if gol == "1" :
        idx = 0
        tunjangan = 0.01
    elif gol == "2" :
        idx = 1
        tunjangan = 0.03
    elif gol == "3" :
        idx = 2
        tunjangan = 0.05 
    else:
            print("Tidak ada dalam pilihan. Silahkan input ulang.")
        
    #tunjangan istri
    if sts_kwn == "kawin":
        if jns_klmn == "laki-laki" and sts_kwn == "kawin":
            tun_istri = tunjangan * int(pokok[idx])
    else:
            tun_istri = 0
        
    #tunjangan anak
    if anak == "y" and sts_kwn == "kawin" :
            tun_anak = 0.02 * int(pokok[idx])
    else:
            tun_anak = 0

    #gaji bruto
    bruto = int(pokok[idx]) + int(tun_istri) + int(tun_anak)

    #gaji netto
    jab = 0.005 * bruto
    pensiun = 15500
    orgns = 3500
    netto = bruto - jab - pensiun - orgns
    
    #interface 
    x = datetime.datetime.now()
    print(x.strftime("%A,%d-%B-%Y ; %H:%M"))
    print("=================================")
    print(" SLIP GAJI KARYAWAN ")
    print("==================================")
    print("Nama             : ", nama)
    print("Golongan         : ", gol)
    print("Jenis Kelamin    : ", jns_klmn)
    print("Status Kawin     : ", sts_kwn)
    print("Gaji Pokok       : Rp.",str(format(pokok[idx],',.2f')))
    print("Tunjangan Istri  : Rp.",str(format(tun_istri,',.2f')))
    print("Tunjangan Anak   : Rp.",str(format(tun_anak,',.2f')))
    print("Gaji Bruto       : Rp.",str(format(bruto,',.2f')))
    print("===================================")
    print("Biaya Jabatan    : Rp.",str(format(jab,',.2f')))
    print("Iuran Pensiun    : Rp.",str(format(pensiun,',.2f')))
    print("Iuran Organisasi : Rp.",str(format(orgns,',.2f')))
    print("Gaji Netto       : Rp.",str(format(netto,',.2f')))
    print("===================================") 
    

    #pengulangan program
   
    jwb = input("Ulangi Program (Y/T) ? = ")
    if jwb == "t" or jwb == "T" :
        break
    else :
            print("Tidak ada pilihan! Silahkan input ulang.")
            