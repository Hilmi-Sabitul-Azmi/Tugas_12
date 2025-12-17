# sistem manajemen nilai mahasiswa

import os
os.system('cls')

file_name = 'rekap_nilai.csv'
if not os.path.exists(file_name):
    with open(file_name,'w') as f:
        f.write('Nama,Nilai_Tugas,Nilai_UTS,Nilai_UAS,Rata-Rata\n')


def input_data():
    banyak = int(input('masukkan jumlah mahasiswa yang akan di input : '))

    with open('rekap_nilai.csv','a') as f:
        for i in range(banyak):
            nama = input('masukkan nama mahasiswa : ').title()
            tugas = int(input('masukkan nilai tugas : '))
            uts = int(input('masukkan nilai UTS : '))
            uas = int(input('masukkan nilai UAS : '))
            rata = round((tugas + uts + uas) / 3,2)

            f.write(f'{nama},{tugas},{uts},{uas},{rata}\n')


def tampil_data():
    from tabulate import tabulate
    headers = []
    rows = []

    with open(file_name, 'r', encoding='utf-8-sig') as f:
        for i, line in enumerate(f):
            kolom = line.strip().split(',')
            if i == 0:
                headers = kolom          # header CSV
            else:
                if len(kolom) == 5:      # validasi data
                    rows.append(kolom)

    print('\n=== REKAP NILAI MAHASISWA ===')
    print(tabulate(rows, headers=headers, tablefmt='grid'))


def cari_data():
    from tabulate import tabulate
    headers = []
    rows = []

    with open(file_name, 'r', encoding='utf-8-sig') as f:
        for i, line in enumerate(f):
            kolom = line.strip().split(',')
            if i == 0:
                headers = kolom          # header CSV
            else:
                if len(kolom) == 5:      # validasi data
                    rows.append(kolom)
                    
    cari = input('\nmasukkan nama mahasiswa yang ingin di cari : ').title()

    hasil = []
    for row in rows:
        if cari in row[0]:
            hasil.append(row)

    if hasil:
        print('\ndata ditemukan')
        print(tabulate(hasil,headers=headers,tablefmt='grid'))
    else:
        print('data tidak di temmukan')


while True:
    print('=====Menu=====')
    print('1. input data')
    print('2. tampilkan data')
    print('3. cari data')
    print('4. keluar')

    pilih = input('pilih menu (1-4) : ')

    if pilih == '1':
        input_data()
        input('\nTekan Enter untuk kembali ke menu...')
    elif pilih == '2':
        tampil_data()
        input('\nTekan Enter untuk kembali ke menu...')
    elif pilih == '3':
        cari_data()
        input('\nTekan Enter untuk kembali ke menu...')
    elif pilih == '4':
        print('\nTerima kasih!')
        break
    else:
        print('\nPilihan tidak valid.')
        input('Tekan Enter untuk ulangi...')

