def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(5,5)

print(retorno)

# ou

def soma(numero1, numero2):
    resp = numero1 + numero2
    print (resp)

retorno = soma(5,5)

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else: 
        return False
    
print (tem_sete_itens('oi sara'))
    

# atividade7
numeros = {1 , 2, 3, 4, 5, 6, 7, 8, 9, 10}
def menor_numero(numeros):
    return min(numeros)
   
print ("O menor número é:", min(numeros))

def maior_numero(numeros):
    return max(numeros)

print("O maior número é:", max(numeros))