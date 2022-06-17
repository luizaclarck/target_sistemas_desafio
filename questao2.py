def sequencia_fibonacci(n):
    if n > 1:
        return sequencia_fibonacci(n-1) + sequencia_fibonacci(n-2)
    return n
    
numero_para_verificar = 11
resultado = 'Numero nao pertence a sequencia'
    
for i in range(15):
    if (sequencia_fibonacci(i) == numero_para_verificar):
       resultado = 'Numero pertence a sequencia'
       
print(resultado)
