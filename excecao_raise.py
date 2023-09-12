#raise provoca excecao
while True:
    try:
        a = int(input('Numero: '))
        b = int(input('Numero: '))
        if a < 0 or b < 0:
            raise ValueError
        c = a/b
        print (c)
    except ValueError:
        print('Erro. Valor invalido')
    except ZeroDivisionError:
        print('Erro. Colocou zero o mula desgracenta')
    except TypeError:
        print('Erro sem solução brotherrr')
    except Exception:
        print('Erro inesperado brotherrr')
    else:               #só executa se n entrar na excessao
        print('É isso cachorro')
        break
