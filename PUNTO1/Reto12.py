# Punto 2
# Si se introduce algo que no sea una palabra, se detecta este Type-error con el raise, y con el except se "guarda".

def palindrome(word: str) -> bool:  
    word_r=[]
    try:
        if type(word) != str:
            raise TypeError( f"{word} no es una palabra")
        word_n = list(word)    #Se convierte la palabra en una lista de caracteres   
        for i in range(len(word_n),0,-1):
            word_r.append(word_n[i-1])
        if word_n == word_r: #Se iguala la palabra original con la palabra reversada
            return True
        else:
            return False
    except TypeError as error:
        print(f"error: {error}")
        
if __name__=="__main__":
    palindrome(2)
