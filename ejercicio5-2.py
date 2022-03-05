def numeroEsPrimo(numero) :
    for i in range(2, (numero // 2)):
        if(numero%i == 0):
            return False
        else:
            return True


