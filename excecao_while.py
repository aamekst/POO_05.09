



'''
while True:
    try:
        a = int(input('Numero: '))
        b = int(input('Numero: '))
        c = a/b
        print (c)
    except ValueError:
        print('Erro. Valor invalido')
    except ZeroDivisionError:
        print('Erro. Colocou zero o mula desgracenta')
    except Exception:
        print('Erro inesperado brotherrr')
    else:               #só executa se n entrar na excessao
        print('É isso cachorro')
        break

    finally:
        print('Já era dog')
    '''