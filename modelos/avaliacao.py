class Avaliacao:
    notas = []

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
        Avaliacao.notas.append(self)

    @property
    def validar_notas(self):
        for avaliacao in Avaliacao.notas:
            if avaliacao._nota < 0 or avaliacao._nota > 5:
                return f'{self._cliente} a nota precisa ser entre 0 a 5'