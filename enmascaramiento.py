def run():
    password = input ('Ingrese la palabra a enmascarar: ')
    pass_slice = password[-4:]
    print(('#' * (len(password)-4)) + pass_slice)

if __name__ == '__main__':
    run()