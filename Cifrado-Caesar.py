texto = input("ingrese el texto a cifrar/decifrar: ")
cambio = int(input("ingrese su cambio: "))
cifrar_o_decifrar = input("quiere cifrar o decifrar el mensaje? ")


def caesar(txt, shift):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto_cifrado = " "
    for char in txt:
        if not char.isalpha():
            texto_cifrado += char
        else:
            remplazo = abecedario.find(char.lower())
            texto_cifrado += abecedario[(remplazo+shift) % 27]
    return texto_cifrado


if cifrar_o_decifrar == "cifrar":
    txt_cifra = caesar(texto, cambio)
    print(f"Su texto cifrado es {txt_cifra}")
elif cifrar_o_decifrar == "decifrar":
    cambio = cambio * -1
    txt_cifra = caesar(texto, cambio)
    print(f"Su texto decifrado es {txt_cifra}")
else:
    print("Solo puede ingresar la palabra cifrar o decifrar en el paso anterior")
