import re

def es_palindromo(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")# elimina los espacios
    return texto_sin_espacios == texto_sin_espacios[::-1]# -1 es para que se lea de atras hacia adelante


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False
print(es_palindromo("perez serep")) 



#ve si en el texto alguna de las letras se encuentra repetidas si es el caso retorna la letra repetida mas veces,
#  sino retorna none
def primera_letra_repetida(texto):

    texto_minsucula = texto.lower()
    texto_sin_espacios = texto_minsucula.replace(" ", "")
    lista_letras = []
    for letra in texto_sin_espacios:
        if letra in lista_letras:
            return letra
        else:
            lista_letras.append(letra)

    return None



print(primera_letra_repetida("comiendo mucho en el campo en octubre")) 
print(primera_letra_repetida("estafa"))  
print(primera_letra_repetida("me gusta pol")) # None


#convertir horario formato hora 

def convertir_horario(hora):

    hora_lista = hora.split(":")
    if hora[-2:].lower() == "pm":
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0]) + 12)
    else:
        if hora_lista[0] == "12":
            hora_lista[0] = "00"

    hora_convertida = ":".join(hora_lista)

    return hora_convertida[:-2]

print(convertir_horario("12:40AM")) # 00:40
print(convertir_horario("04:59pm")) # 16:59
print(convertir_horario("10:00:00PM")) # 22:00
print(convertir_horario("22:00:00PM")) # no funciona regis areglando
print(convertir_horario("10:00:00")) # no funciona 

# anagrama que se 2 palabras cuenten con iguaes letras en diferente orden
def es_anagrama(palabra_1, palabra_2):

    letras_palabra_1 = sorted(palabra_1.lower())
    letras_palabra_2 = sorted(palabra_2.lower())

    return letras_palabra_1 == letras_palabra_2


print(es_anagrama("lama", "Mala"))   # True
print(es_anagrama("calor", "coral")) # True
print(es_anagrama("cama", "casa"))   # False
print(es_anagrama("las", "sal"))

# cambiar caracteres especiales por guion para ello se inporta re
def slugify(texto):

    slug = (texto
        .lower()
        .strip()
        .replace(" ", "-")
    )

    slug = re.sub("[^\w\-]", "", slug)
    return slug
texto = input("ingresa un texto en cosola con caracteres especiales")
print(slugify(texto))
print(slugify("texto% con caracteres$# especial-es")) # texto-con-caracteres-especial-es
print(slugify("Este es un ejemplo!!!")) # este-es-un-ejemplo

# muestra si el codigo se encuentra con con los parantisin adecuados
def parentesis_balanceados(texto):

    apertura = 0

    for parentesis in texto:
        if parentesis == "(":
            apertura += 1
        elif parentesis == ")":
            apertura -= 1

            if apertura < 0:
                return False

    return apertura == 0


print(parentesis_balanceados("((()))()"))
print(parentesis_balanceados(")(()"))
print(parentesis_balanceados("(()"))
