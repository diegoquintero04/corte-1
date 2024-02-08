# #Fahrenheit a Celsius
# print("Transformador de Fahrenheit a Celsius")
# F = float(input("Ingrese los Fahrenheit aqui: "))
# C = (F - 32) * 5/9
# print(f"Los {F} Fahrenheit son {round(C,2)} grados Celsius!")

# #Calcular producto + IVA
# print("Calcular producto + IVA del 19%")
# valor = float(input("Ingrese el valor del producto: "))
# total = valor*1.19
# print(f"El producto con valor {valor}, mas IVA es: {total}")

#Hallar divisores
print("Hallar divisores de un numero")
num = int(input("Ingrese un numero para hallar divisores: "))
divisores = []
# for i in range(1,num+1):
#     if num % i == 0:
#         divisores.append(i)        
# print(divisores)

i = 1
while i <= num:
    if num % i == 0:
        divisores.append(i)
    i += 1
print(divisores)        









