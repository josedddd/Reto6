#Punto 4
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