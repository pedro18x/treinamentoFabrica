    

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 == num2 and num2 == num3:
    print("Três iguais")
elif num1 == num2 or num1 == num3 or num2 == num3:
    if num1 != num2 and num1 != num3 and num2 != num3:
        print("Dois diferentes")
    else:
        print("Dois iguais")    

else:
    print("Três diferentes")