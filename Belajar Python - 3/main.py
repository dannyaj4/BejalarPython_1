# a = 12 (a merupakan variable dan 12 merupakan value bernilai integer)
# Tipe data Python

# Tipe data: Integer / Angka Satuan
data_int = 1 
print("data: ", data_int)  
print("-tipe data:", type(data_int))
# Pada python angka 1 otomatis dianggap integer, tidak seperti bahasa pemograman lain
# type(variable) digunakan untuk melihat tipe data 

# Tipe data: Float / Bilangan koma
data_float = 1.5
print("data: ", data_float)
print("-tipe data: ", type(data_float))

# Tipe data: String / kumpulan karakter dalam ""
data_string = "Seminar"
print("data: ", data_string)
print("-tipe data: ", type(data_string))

# Tipe data: Boolean / binary code 0 or 1 / as biner true or false
data_bool = True
print("data: ", data_bool)

## Tipe data Khusus

# Bilangan kompleks / bilangan imajiner
data_complex = complex(1,1)
print("data : ", data_complex)
print("-tipe data: ", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.432)
print("data: ", data_c_double)
print("-tipe data: ", data_c_double)