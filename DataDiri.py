inputan_data = {                                        # Program Data Diri 
	'Nama' : [],
    'Umur' : [],
    'Hobi' : []
    }

def menu_input():                                       # Program utama
    print("\n==========Menu==========")
    print("silahkan input data diri")
    print("1. Daftar List")
    print("2. Tambah data")
    print("3. Delete data")
    print("4. Exit")
    
    Pilihan = input("masukan pilihan [1/2/3/4]:" )
    if Pilihan == "1":
        DaftarInput()
    elif Pilihan == "2":
        Tambah()
    elif Pilihan == "3":
        Delete()
    else: 
        Exit()


def DaftarInput():                                      # Menampilkan isi list
    print("\n===========Total List==========")
    print(inputan_data['Nama'])
    print(inputan_data['Umur'])
    print(inputan_data['Hobi'])

    # kembali ke menu
    menu_input()

def Tambah():                                           # Menambahkan inputan/nilai
    print("\n=========Input Data Diri=======")
    inputan_data['Nama'].append(input("Nama: "))
    inputan_data['Umur'].append(input("Usia: "))
    inputan_data['Hobi'].append(input("Hobi: "))
    
    # kembali ke menu
    menu_input()

def Delete():                                           # Mengurangi inputan/nilai
    print("\n========Update Data Diri=======")
    inputan_data['Nama'].remove(input("Nama: "))
    inputan_data['Umur'].remove(input("Usia: "))
    inputan_data['Hobi'].remove(input("Hobi: "))
    
    # kembali ke menu
    menu_input()

def Exit():                                             # Keluar program
    while True:
        input_lagi = input('tidak ada tambahan lagi? (y/n): ')    
        if input_lagi == "y":
            menu_input()    
        else:
            break


if __name__ == "__main__":
    menu_input()