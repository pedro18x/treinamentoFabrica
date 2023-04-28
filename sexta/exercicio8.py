
frase = "treinamento hoje de backend"

print("Frase original:", frase)

palavra_antiga = input("Digite a palavra que deseja trocar: ")
nova_palavra = input("Digite a nova palavra: ")

nova_frase = frase.replace(palavra_antiga, nova_palavra)

print("Nova frase:", nova_frase)