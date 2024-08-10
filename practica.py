# ejercicio para practicar python

#FORMA RECURSIVA DE REALIZAR EL PROYECTO
def sumNum(num):
    if num == 1:
        return 1
    else:
        return num + sumNum(num - 1)

print(sumNum(10))
