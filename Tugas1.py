total_list = {
	'makanan' : ['roti', 'kacang'],
    'minuman' : ['teh botol', 'kopi']
    }


def tampilan_menu():
    #menampilkan item    
    daftar_item = show_item()
    #tambah item
    add_item = tambah_item()
    #hapus item
    del_item = delete_item()
    #update
    update = update_item()
    #selesai
    keluar = exit()    

def show_item():
    print("\n=====Daftar List=====")
    print("list makanan: ",total_list['makanan'])
    print("list minuman: ",total_list['minuman'])
        #return (tampilan_menu)

def tambah_item():
    print("\n=====tambah item=====")
    tambah_item = input("tambah makanan/minuman [0/1]: ")
    if tambah_item == "0":
        total_list['makanan'].append(input("tambah makanan: "))
        print("list makanan: ",total_list['makanan'])
            #return
    else:
        total_list['minuman'].append(input("tambah minuman: "))
        print("list minuman: ",total_list['minuman'])
            #return

def delete_item():
    print("\n=====hapus item=====")
    delete_item = input("hapus makanan/minuman [0/1]: ")
    if delete_item == "0":
        total_list['makanan'].remove(input("hapus makanan: "))
        print("list makanan: ",total_list['makanan'])
            #return
    else:
        total_list['minuman'].remove(input("hapus minuman: "))
        print("list minuman: ",total_list['minuman'])
            #return

def update_item():
    print("\n=====Update Stok=====")
    print("list makanan: ",total_list["makanan"])
    print("list minuman: ",total_list["minuman"])
        #return

def exit():
    print("\n=====lanjut / selesai=====")
    exit = input("lanjut update stok[Yes/No]: ")
    if exit == "Yes":
        tampilan_menu()
    else:
        print("\n=====Update selesai=====")
        print("list makanan: ",total_list["makanan"])
        print("list minuman: ",total_list["minuman"])      

if __name__ == "__main__":
    tampilan_menu()
