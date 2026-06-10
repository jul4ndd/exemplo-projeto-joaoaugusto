from imagem import Imagem
from pdf import Pdf

if __name__ == '__main__':

    imagem = Imagem()
    pdf = Pdf()

    for i in range(2):
        print(pdf.exibir())
        print(imagem.exibir())
        print('-------------------')
            