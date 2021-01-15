# Casting Tipe Data
# Merubah tipe data satu ke tipe lainnya
# Operator Casting float, int, boolean, str

data_int = 9; 
print("data = ", data_int, ", tipe data = ", type(data_int))


data_float = float(data_int)
print("data = ", data_float, ", tipe data = ", type(data_float))

# Input User

data = input("Masukkan data: ")
#data yang dimasukkan pasti string
print("data =", data, ", tipe data =", type(data)) 

#bila mau mengambil integer
data_int = int(input("masukkan angka: "))
print("data =", data_int, type(data_int))


#data boolean
data_bool = bool(int(input("Masukkan data anda: ")))
print("data =", data_bool, type(data_bool))


