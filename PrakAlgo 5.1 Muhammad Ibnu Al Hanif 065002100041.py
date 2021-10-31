print ("@  @    @    @   @   @   @@@")
print ("@  @   @ @   @@  @   @   @  ")
print ("@@@@  @@@@@  @ @ @   @   @@ ")
print ("@  @ @     @ @   @   @   @  ")

a = int(input("Masukan jumlah bilangan: "))
while a<2:
  print("Salah")
  a = int(input("Masukan jumlah bilangan: "))
F1 = int(input("Masukan angka pertama: "))
F2 = int(input("Masukan angka kedua: "))
for i in range(a):
  v=F1
  
  x = F1+F2
  F1=F2
  F2=x
  print('Berikut urutannya')
  print(v)