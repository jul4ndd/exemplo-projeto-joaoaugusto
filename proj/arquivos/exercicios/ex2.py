def ler_poema():
    try:
        with open('proj/arquivos/exercicios/arquivos/poema.txt', 'r') as poema:
            texto = poema.read()
        return texto
    except FileNotFoundError:
        print("Arquivo não encontrado")

if __name__ == '__main__':
    poema = ler_poema()
    print(poema)