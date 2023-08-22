class DataDiri:                                         # Program Data Diri       
    def __init__(self, Nama, Umur, Hobi):
        self.Nama = Nama
        self.Umur = Umur
        self.Hobi = Hobi

    def getNama(self):
        return self.Nama
    
    def getUmur(self):
        return self.Umur
    
    def getHobi(self):
        return self.Hobi
    
    def setNama(self,Nama):
        self.Nama = Nama
    
    def setNama(self,Umur):
        self.Umur = Umur

    def setNama(self,Hobi):
        self.Hobi = Hobi

inputan_data = {                                        # Input nilai/data
	    }

loop = True

print("\n==========Menu==========")
print("silahkan input data diri")
print("1. Daftar List")
print("2. Tambah data")
print("3. Delete data")
print("4. Exit")

while(loop):

    Pilihan = input("\nmasukan pilihan [1/2/3/4]:")
    if Pilihan == "1":                                  # Menampilkan daftar list
        print("========Daftar List========")
        for x in inputan_data:
            print("Nama : ", inputan_data[x].getNama())
            print("Umur : ", inputan_data[x].getUmur())
            print("Hobi : ", inputan_data[x].getHobi())
            
    elif Pilihan == "2":                                # Menambahkan inputan/nilai
        print("========Tambah data========")
        Nama = input("Nama : ")
        Umur = input("Umur : ")
        Hobi = input("Hobi : ")
        masukan = DataDiri(Nama, Umur, Hobi)
        inputan_data[Nama] = masukan 
            
        
    elif Pilihan == "3":                                # Mengurangi inputan/nilai
        print("========Delete data========")
        Nama = input("Nama yg mau di delete : ")
        if Nama in inputan_data:
            del inputan_data[Nama]
        else:
            print("Nama yg diinput ga ada")
            
    else:                                               # keluar program
        #loop = False
        print("===========Exit===========")
        input_lagi = input('tidak ada tambahan lagi? (y/n): ')    
        if input_lagi == "y":
            loop = True    
        else:
            loop = False