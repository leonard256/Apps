#Calcula el Indice de Masa Corporal

def main():
    peso = float(input('Ingrese su peso en kg: '))
    altura = float(input('Ingrese su altura en metros: '))

    imc = peso/(altura)**2
    imc = round(imc,1)
    print(f'Su indice de masa corporal es {imc}')

    if 18 <= imc <= 24:
        print('Su peso es normal, puede considerarse una persona sana')
    elif  25 <= imc <= 29:
        print('Padece de SOBREPESO, Sin embargo, no padece obesidad\nSe recomienda realizar cambios saludables con su alimentación e incluir rutinas de ejercicio fisico')
    elif  30 <= imc <= 35:
        print('Padece de OBESIDAD\nLa obesidad se considera una enfermedad del organismo, con todo lo que ello conlleva, y además es un proceso crónico y progresivo')
    elif  36 <= imc <= 40:
        print('Padece de OBESIDAD SEVERA')
    elif  imc > 40:
        print('Padece de OBESIDAD MORBIDA')
    else:
        print('Los datos ingresados son erroneos')

if __name__ == '__main__':
    main()



