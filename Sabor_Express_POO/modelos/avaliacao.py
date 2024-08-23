class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente # Nome do cliente que fez a avaliação
        self._nota = nota # Nota dada pelo cliente

    # Método para converter o objeto Avaliação em um dicionario para salvar em JSON
    def __dict__(self):
        return{
            'cliente': self._cliente,
            'nota': self._nota
        }
