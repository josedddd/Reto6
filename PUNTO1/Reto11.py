#Punto 1
# Por cada operacion se hace con un match y un case, y se asigna el resultado la correspondiente operacion
# Si en la entrada, se pone algo que no sea un float o un int, o existe una division por 0
# se detecta y se "guarda" este error, evitando una interrupcion brusca, se usa tanto try-except como raise.

def operations(num1: float, num2: float, op: str): 
    try:
        if not isinstance(num2, (float, int)) or not isinstance(num1, (float,int)):
            raise TypeError("tipo de entrada incorrecta")
        match op:
            case "+":               #Caso de la suma
                result = num1+num2  
            case "-":               #Caso de la resta
                result = num1-num2
            case "*":               #Caso de la multiplicacion
                result = num1*num2
            case "/":               #Caso de la division
                if num2 == 0:
                   raise ZeroDivisionError("Estas diviendo por 0")
                result = num1/num2
        return result
    
    except (TypeError,ZeroDivisionError) as error:
        print(f"heyy tienes un error {error}")


if __name__=="__main__":
 print(operations("s",0,"/"))

