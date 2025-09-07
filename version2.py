import random
import datetime
import time

class Produto:
    def __init__(self, nome, preco, avaliacao, data_adicao, categoria):
        self.nome = nome
        self.preco = preco
        self.avaliacao = avaliacao
        self.data_adicao = data_adicao
        self.categoria = categoria
 
    def __repr__(self):
        return f"{self.nome}: {self.preco}, {self.avaliacao}, {self.data_adicao}, {self.categoria}"

def gerar_produtos(n):
    nomes = ["Produto" + str(i) for i in range(n)]
    precos = [round(random.uniform(10, 1000), 2) for _ in range(n)]
    avaliacoes = [round(random.uniform(0, 5), 2) for _ in range(n)]
    datas = [datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 365)) for _ in range(n)]
    categorias = ["Categoria" + str(random.randint(1, 5)) for _ in range(n)]
    
    produtos = [Produto(nomes[i], precos[i], avaliacoes[i], datas[i], categorias[i]) for i in range(n)]
    return produtos

# Exemplo de geração de produtos
produtos = gerar_produtos(1000)
#for produto in produtos[:10]: # Mostrar os 10 primeiros produtos
    #print(produto)
# Implementação do bubble sort

print("################# Tempo de execução do Bubble Sort #################")

n = len(produtos)

def bubble_sort(lista, key, contrario = False):
    inicio = time.time()
    for j in range (n-1):
        for i in range (n-1):
            if (key(lista[i]) > key(lista[i+1])) ^ contrario:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    fim = time.time()
    return fim - inicio

print("1) Por preço:")

print("Ascendente:")
tempo = bubble_sort(produtos, key=lambda p: p.preco, contrario=False)
print(f"Tempo de execução: {tempo:.4f} segundos")
print("Descendente:")
tempo = bubble_sort(produtos, key=lambda p: p.preco, contrario=True)
print(f"Tempo de execução: {tempo:.4f} segundos")

print("----------------------------------------------------------")

print("2) Por avaliacao:")

print("Ascendente:")
tempo = bubble_sort(produtos, key=lambda p: p.avaliacao, contrario=False)
print(f"Tempo de execução: {tempo:.4f} segundos")
print("Descendente:")
tempo = bubble_sort(produtos, key=lambda p: p.avaliacao, contrario=True)
print(f"Tempo de execução: {tempo:.4f} segundos")

print("----------------------------------------------------------")

print("3) Por data de adição:")

print("Mais recente:")
tempo = bubble_sort(produtos, key=lambda p: p.data_adicao, contrario=False)
print(f"Tempo de execução: {tempo:.4f} segundos")
print("Mais antigo:")
tempo = bubble_sort(produtos, key=lambda p: p.data_adicao, contrario=True)
print(f"Tempo de execução: {tempo:.4f} segundos")

print("----------------------------------------------------------")

print("4) Por categoria:")

print("Ordem alfabética:")
tempo = bubble_sort(produtos, key=lambda p: p.data_adicao, contrario=False)
print(f"Tempo de execução: {tempo:.4f} segundos")