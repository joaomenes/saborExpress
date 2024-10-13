from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de laranja', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_italiano = Prato('Bolonhesa', 2.00, 'melhor da cidade')
prato_italiano.aplicar_desconto()
primeira_sobremesa = Sobremesa('Pudim', 30.00, 'Pudim', 'Médio', 'Pudim com creme de leite')
primeira_sobremesa.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_italiano)
restaurante_praca.adicionar_no_cardapio(primeira_sobremesa)



def main():
    restaurante_praca.exibir_cardapio
    

if __name__ == '__main__':
    main()