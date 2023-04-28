
string = input("Digite uma string: ")

palavra = input("Digite uma palavra a ser procurada na string: ")

if palavra in string:
    print("A palavra", palavra, "foi encontrada na string.")
else:
    print("A palavra", palavra, "não foi encontrada na string.")