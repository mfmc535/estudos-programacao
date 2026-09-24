#receber um string que representa uma operação matemática
#tratar os dados de entrada e retornar um resultado em decimal
expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)
if "/" in y:
    print(f"{(x/z):.1f}")
elif "+" in y:
    print(f"{(x+z):.1f}")
elif "-" in y:
    print(f"{(x-z):.1f}")
else:
    print(f"{(x*z):.1f}")