print("-- CALCULADORA --")
numero1 = float(input("Digite o numero 1\n"))

oper = str(input("escolha a operação: (-), (+), (/), (*)\n"))
if oper not in ("-", "+", "/", "*"):
    print("operador invalido!")
    exit()
    
numero2 = float(input("Digite o numero 2\n"))

if oper == "-":
    print(" Seu numero é:", numero1 - numero2)

elif oper == "+":
    print(" Seu numero é:", numero1 + numero2)
    
elif oper == "/":
    print(" Seu numero é:", numero1 / numero2)
    
elif oper == "*":
    print("Seu numero é:", numero1 * numero2)
    
else:
    print("erro")