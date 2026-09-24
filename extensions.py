#Identificar a extensão digitada
#Depois retornar o tipo de arquivo executado/extensão.
tipo = (input("File name: ")).split(".", 1)[1]
if tipo == "jpg" or tipo == "jpeg" or tipo == "gif":
    print(f"image/{tipo}")
elif "pdf" in tipo:
    print("application/pdf")
else:
    print("application/octet-stream")