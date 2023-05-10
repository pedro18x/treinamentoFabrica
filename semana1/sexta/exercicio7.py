frase = input("Digite uma frase: ")

frase_sem_espacos = frase.replace(" ", "")

num_caracteres = len(frase_sem_espacos)

# exibe a frase e a quantidade de caracteres
print("A frase digitada foi:", frase)
print("A quantidade de caracteres (sem espaços) é:", num_caracteres)