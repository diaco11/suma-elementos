#FUNCION FACTORIAL

def factorial(num:int):
    #CASO BASE
    if num == 0:
        return 1
    #CASO RECURSIVO
    else:
        return num * factorial(num  - 1)
    

print(factorial(5))    