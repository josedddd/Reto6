def prime(list_num: list):
    prime_num=[]  
    for num in list_num:
        try:
            if not isinstance(num, int):
                raise TypeError(f"  {num} no es un numero entero")
            remainders = [num % i for i in range(2, num)]
            if all(remainders):
                prime_num.append(num)
        except TypeError as error:
            print(f"Error: {error}")
    return prime_num 

if __name__=="main":
    print(prime([2,6,7,1.4]))