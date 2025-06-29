#Punto 5
#En este codigo, al igual que el anterior, si la lista no es suficientemente grande, genera un Indexerror porque el codigo no puede funcionar
#Con el try-except, es lo mismo que el anterior, si lo que se introduce no es una palabra se usa el except para "guardar" el error y que el 
#codigo pueda funcionar normalmente, y detectar si las palabras tienen la misma cantidad.

def equal(list_word: list):
    list_equal_length = []
    if len(list_word) < 2:
        raise IndexError("No hay suficientes palabras :v")
    # Recorro la lista de palabras
    for i in range(0,len(list_word)):
        for j in range(i+1,len(list_word)):
        # Compruebo si las palabras tienen la misma longitud     
            try:
                word1=list_word[i]
                word2=list_word[j]
                if not isinstance(word1, str ) or not isinstance(word2, str ):
                        raise TypeError(f"{word1} o {word2} No es una palabra")
                if len(list_word[i])==len(list_word[j]):
                # Si aún no están en la lista, las agrego
                    if list_word[i] not in list_equal_length:
                        list_equal_length.append(list_word[i])
                    if list_word[j] not in list_equal_length:
                        list_equal_length.append(list_word[j])
            except TypeError as error:
                print(f"error:{error}")
    return list_equal_length

if __name__=="main":
    print(equal(["hola","helo",2,"carro"]))
