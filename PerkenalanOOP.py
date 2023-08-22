class Perkenalan:
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


inputan_biodata = {
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
    if Pilihan == "1":
        for x in inputan_biodata:
            print("Nama : ", inputan_biodata[x].getNama())
            print("Umur : ", inputan_biodata[x].getUmur())
            print("Hobi : ", inputan_biodata[x].getHobi())
            
    elif Pilihan == "2":
        Nama = input("Nama : ")
        Umur = input("Umur : ")
        Hobi = input("Hobi : ")
        DataDiri = Perkenalan(Nama, Umur, Hobi)
        inputan_biodata[Nama] = DataDiri 
            
        
    elif Pilihan == "3":
        Nama = input("Nama yg mau di delete : ")
        if Nama in inputan_biodata:
            del inputan_biodata[Nama]
        else:
            print("Nama yg diinput ga ada")
            
    else:
        #loop = False
        input_lagi = input('tidak ada tambahan lagi? (y/n): ')    
        if input_lagi == "y":
            loop = True    
        else:
            loop = False