#-----------------------[ PROGRAM MATEMATIKA ]--------------------#
#!/usr/bin/python3
#Code By Rehan
def tambah(x,y):
	return x + y
def kurang(x,y):
	return x - y
def kali(x,y):
	return x * y
def bagi(x,y):
	return x / y
logo = """  _         _ _          _       _             
 | |       | | |        | |     | |            
 | | ____ _| | | ___   _| | __ _| |_ ___  _ __ 
 | |/ / _` | | |/ / | | | |/ _` | __/ _ \| '__|
 |   < (_| | |   <| |_| | | (_| | || (_) | |   
 |_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|   
                                               
                                               """
def menu():
	print(logo)
	print("="*60)
	print("                   \033[2;97m[\033[2;92m•\033[2;97m] AUTHOR : \033[2;92mRehan  \033[2;97m[\033[2;92m•\033[2;97m]\n          \033[2;97m[\033[2;92m•\033[2;97m] GITHUB : \033[2;92mhttps://github.com/R3HAN6 \033[2;97m[\033[2;92m•\033[2;97m]")
	print("="*60)
	print("\033[2;97m[\033[2;92m01\033[2;97m] TAMBAHAN")
	print("\033[2;97m[\033[2;92m02\033[2;97m] PENGURANGAN")
	print("\033[2;97m[\033[2;92m03\033[2;97m] PERKALIAN")
	print("\033[2;97m[\033[2;92m04\033[2;97m] PEMBAGIAN")
	print("="*60)
	Rehan = input("\n\033[2;97m[\033[2;92m•\033[2;97m] choice: ")
	if Rehan == "":
		print("\033[2;97m[\033[2;92m•\033[2;97m] Ngetik Apaan Luh Bangsad :v")
		exit()
	elif Rehan =="1":
		x()
	elif Rehan == "2":
		xx()
	elif Rehan == "3":
		xxx()
	elif Rehan == "4":
		xxxx()
	else:
		print("\033[2;97m[\033[2;92m•\033[2;97m] Ngetik Apaan Luh Bangsad :v")
#---------------------------------[ TAMBAH ]----------------------------------#
def x():
	angka1 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Pertama: "))
	angka2 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Kedua: "))
	print("\033[2;97m[\033[2;92m√\033[2;97m]",angka1,"+",angka2,"=",tambah(angka1,angka2))
#-----------------------------[ PENGURANGAN ]----------------------------#
def xx():
	angka1 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Pertama: "))
	angka2 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Kedua: "))
	print("\033[2;97m[\033[2;92m√\033[2;97m]",angka1,"-",angka2,"=",kurang(angka1,angka2))
#--------------------------------[ PERKALIAN ]--------------------------------#
def xxx():
	angka1 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Pertama: "))
	angka2 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Kedua: "))
	print("\033[2;97m[\033[2;92m√\033[2;97m]",angka1,"x",angka2,"=",kali(angka1,angka2))
#--------------------------------[ PEMBAGIAN ]-------------------------------#
def xxxx():
	angka1 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Pertama: "))
	angka2 = int(input("\033[2;97m[\033[2;92m•\033[2;97m] Masukan Angka Kedua: "))
	print("\033[2;97m[\033[2;92m√\033[2;97m]",angka1,"÷",angka2,"=",bagi(angka1,angka2))

if __name__ == "__main__":
	menu()