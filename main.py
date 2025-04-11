def suma_digitos(n):
    if n<10:
        return n 
    return (n%10) +suma_digitos(n//10)

# Ejemplo:
print(suma_digitos(123))          # 6
print(suma_digitos(9))            # 9