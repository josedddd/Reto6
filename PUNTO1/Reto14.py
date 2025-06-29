#Punto 4
# Primero si en la lista no hay dos numeros o mas, genera un Index-error con el raise, porque el programa no puede funcionar. Luego con el try-except, se detecta el tipo de 
# los elementos de la lista, y si alguno no es entero, simplemente el except lo "guarda" haciendo que el codigo pueda correr, y detectar la mayor suma entre los enteros que halla

def maxsum(list_num: list):
    consecutive_sum=[]
    if len(list_num) < 2:
        raise IndexError("no hay suficientes numeros")
    for i in range(1,len(list_num)):
        try:
            numer=list_num[i]
            numer2=list_num[i-1]
            if not isinstance(numer, int) or not isinstance(numer2, int):
                raise TypeError(f"Tipo de dato incorrecto entre {numer} y {numer2}")
            consecutive_sum.append(list_num[i]+list_num[i-1])
        except (TypeError, IndexError) as error:
            print(f"error:{error}")
    return max(consecutive_sum) 



if __name__=="main":
    print(maxsum([5,3,4,"hola"]))
