
def funcao_1():
        print('Início da função')
        lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        try:
            for i in range(15):
                print(lista[i])
        except IndexError:
                print('Numero de itens menor que o solicitado')
        finally:
              print('Fim da função')


funcao_1() 
