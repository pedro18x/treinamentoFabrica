
string = input("Digite uma string: ")


num_letras = 0


for caractere in string:

    if caractere.isalpha():
    
        num_letras += 1

print("A string digitada contém", num_letras, "letras.")