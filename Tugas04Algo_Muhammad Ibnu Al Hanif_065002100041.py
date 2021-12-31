mahasiswa=[['Joni Junior',75,80,65,],['Edwin',85,85,90,],['Reina Ayu',50,60,60,],['Daniel',90,85,95,],['Zachy',50,50,50]]

def lihat_nilai():
    nama=input("Nama Mahasiswa: ")
    for i in mahasiswa:
        if i [0]== nama:
            print(i)
    menu()
def view_data():
    print(" NAMA |","PRAK 1|","PRAK 2|","PRAK 3|")
    for i in mahasiswa:
        print(i[0],"     ",i[1],"     ",i[2],"     ",i[3],)
    menu()
def update_nilai():
    update=input("Nama Yang Dicari :")
    nilai=int(input("Ingin Update nilai Praktikum ke-: "))
    nilai_baru=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    menu()
def hapus_data():
    hapus=input("Masukkan Nama Mahasiswa Yang Ingin di hapus: ")
    for i in mahasiswa:
        if i [0]== hapus:
            mahasiswa.remove(i)
    menu()
def simpan_file():
    file=open("tugas04algo.txt","w")
    file.write(" NAMA |"+"PRAK 1|"+"PRAK 2|"+"PRAK 3|")
    for i in mahasiswa:
        file.writelines(i[0]+"     "+str(i[1])+"     "+str(i[2])+"     "+str(i[3]))
    file.close()
    menu()
def menu():
    print("Program List")
    print("1.LIHAT NILAI")
    print("2.UPDATE NILAI")
    print("3.HAPUS DATA")
    print("4.VIEW DATA")
    print("5.SIMPAN FILE ")
    
    print("6.EXIT")
    pilih=int(input("Pilih Menu Yang Tersedia:"))
    if pilih==1:
        lihat_nilai()
    elif pilih==2:
        update_nilai()
    elif pilih==3:
        hapus_data()
    elif pilih==4:
       view_data()
    elif pilih==5:
        simpan_file()
    else:
        print("Terima Kasih :)")
        exit()
menu()