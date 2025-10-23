def es_palindroma(frase: str) -> bool:
    frase = frase.replace(' ', '')
    frase = frase.lower()
    tildes = {'á': 'a','é': 'e', 'í': 'i', 'ó': 'o', 'ú':'u'}

    parseada = ''
    for i in range(len(frase)):
        if frase[i] in tildes:
            parseada += tildes[frase[i]]
        else:
            parseada += frase[i]
    return parseada == parseada[::-1]

def palabras_impares(frase:str) -> bool:
    lista = frase.split(" ")
    return lista[::2]
def primera_palabra(frase:str) -> str:
    return frase.split(" ")[0]
def ultima_frase(parrafo:str) -> str:
    return parrafo.split(".")[-2]
# print(primera_palabra("Hola mundo como va todo"))
def es_primo(numero: int) -> bool:
    if numero == 1:
        return False
    for i in range(numero):
        for j in range(numero):

            print(i, j)
            if (i * j) == numero and (i != 1 or j != numero or i != numero or j != 1):
                return False
            
    return True
print(ultima_frase("Hola mundo. como va todo."))

print(es_primo(30))