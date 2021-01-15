# Conversi satuan Celcius ke R F K
# Conversi satuan temperatur

print("\nProgram Konversi Temperature\n")

celcius = float(input('Masukkan Suhu dlm Celcius: '))
print("Suhu adalah: ", celcius, "Celcius")

#Reamur
reamur = (4 / 5) * celcius
print("Suhu reamur: ", reamur, "Reamur") 

#Fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu fahrenheit: ", fahrenheit, "Fahrenheit") 

#Kelvin
kelvin = celcius + 273
print("Suhu kelvin: ", kelvin, "Kelvin") 
