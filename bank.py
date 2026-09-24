# imprimir $0 se o string conter "Hello"
# $20 se for diferente de "Hello" mas iniciar com "H"
# $100 se nenhuma das alternativas
frase = str(input("Greeting: "))
if "Hello" in frase:
    print("$0")
elif frase.count("H", 0, 1) == 1:
    print("$20")
else:
    print("$100")