mahasiswa=[['Joni Junior',75,80,65,],['Edwin',85,85,90,],['Reina Ayu',50,60,60,],['Daniel',90,85,95,],['Zachy',50,50,50]]

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
def rata_mahasiswa():
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        print(mahasiswa[i][0],"=",total/len(mahasiswa[i]))
    menu()
def simpan_file():
    file=open("tugas04algo.txt","w")
    file.write(" NAMA |"+"PRAK 1|"+"PRAK 2|"+"PRAK 3|")
    for i in mahasiswa:
        file.writelines(i[0]+"     "+str(i[1])+"     "+str(i[2])+"     "+str(i[3]))
    file.close()
def menu():
    print("Program List")
    print("1.LIHAT NILAI")
    print("2.RATA-RATA NILAI MAHASISWA:")
    print("3.UPDATE NILAI")
    print("4.SIMPAN FILE")
    
    print("5.EXIT")
    pilih=int(input("Pilih Menu Yang Tersedia:"))
    if pilih==1:
        view_data()
    elif pilih==2:
        rata_mahasiswa()
    elif pilih==3:
        update_nilai()
    elif pilih==4:
       simpan_file()
    else:
        print("Terima Kasih :)")
        exit()
menu()