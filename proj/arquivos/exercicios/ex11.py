def mapear_paredes_planta(nome_arquivo: str):
    try:
        coordenadas = []
        with open(nome_arquivo) as planta:
            
            for index_linha, linha in enumerate(planta.readlines()):
                for index_coluna, caracter in enumerate(linha):
                    if caracter == '=':
                        coordenadas.append((index_linha,index_coluna))
        
        return coordenadas
    except FileNotFoundError:
        return 'arquivo não encontrado'
    
if __name__ == '__main__':
    coordenadas = mapear_paredes_planta(
        'proj/arquivos/exercicios/arquivos/planta_casa.txt')
    print(coordenadas)