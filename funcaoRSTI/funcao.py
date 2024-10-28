def somar_dois_numeros(a, b):
    resultado = a + b
    return resultado

def triploSomar(soma):
    x = soma * 3
    return x

a = float(input("digite o primeiro valor: "))
b = float(input("digite o segundo valor: "))

soma = somar_dois_numeros(a, b)
triploX = triploSomar(soma)

print("Soma: ", soma)
print("triplo: ", triploX)