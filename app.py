from modelos.restaurante import Restaurante

mensagem = restaurante_praca = Restaurante('praça', 'Gourmet')
mensagem = restaurante_praca.receber_avaliacao('Gui', 3)
mensagem = restaurante_praca.receber_avaliacao('Lais', 6)
mensagem = restaurante_praca.receber_avaliacao('Emy', 15)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()