# ejercicio para practicar python

#FORMA RECURSIVA DE REALIZAR EL PROYECTO
def sumNum(num:int) -> int:
    #caso base
    if num == 1:
        return 1
    #caso recursivo
    else:
        return num + sumNum(num - 1)

print(sumNum(10))
