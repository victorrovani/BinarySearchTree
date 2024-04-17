class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, dado):
        if self.cabeca is None:
            self.cabeca = No(dado)
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = No(dado)

class NoArvore:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

def inserir_arvore(raiz, chave):
    if raiz is None:
        return NoArvore(chave)
    else:
        if raiz.valor < chave:
            raiz.direita = inserir_arvore(raiz.direita, chave)
        else:
            raiz.esquerda = inserir_arvore(raiz.esquerda, chave)
    return raiz

def percurso_in_order(raiz):
    return percurso_in_order(raiz.esquerda) + [raiz.valor] + percurso_in_order(raiz.direita) if raiz else []

# Exemplo de uso
palavras = ListaEncadeada()
raiz = None

# Inserindo palavras
for palavra in ["banana", "maçã", "cereja", "rocambole", "acarajé", "pizza", "hambúrguer"]:
    palavras.inserir(palavra)
    raiz = inserir_arvore(raiz, palavra)

# Imprimir palavras em ordem alfabética
palavras_ordenadas = percurso_in_order(raiz)
print("Palavras em ordem alfabética:", palavras_ordenadas)
