inputan_biodata = {
	'Nama' : [],
    'Umur' : [],
    'Hobi' : []
    }

def menu_input():
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


def DaftarInput():
    print("\n===========Total List==========")
    print(inputan_biodata['Nama'])
    print(inputan_biodata['Umur'])
    print(inputan_biodata['Hobi'])

    # kembali ke menu
    menu_input()

def Tambah():
    print("\n=========Input Data Diri=======")
    inputan_biodata['Nama'].append(input("Nama: "))
    inputan_biodata['Umur'].append(input("Usia: "))
    inputan_biodata['Hobi'].append(input("Hobi: "))
    
    # kembali ke menu
    menu_input()

def Delete():
    print("\n========Update Data Diri=======")
    inputan_biodata['Nama'].remove(input("Nama: "))
    inputan_biodata['Umur'].remove(input("Usia: "))
    inputan_biodata['Hobi'].remove(input("Hobi: "))
    
    # kembali ke menu
    menu_input()

def Exit():
    while True:
        input_lagi = input('tidak ada tambahan lagi? (y/n): ')    
        if input_lagi == "y":
            menu_input()    
        else:
            break


if __name__ == "__main__":
    menu_input()