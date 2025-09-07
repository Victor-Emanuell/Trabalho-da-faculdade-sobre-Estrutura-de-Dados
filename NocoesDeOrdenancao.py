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
produtos = gerar_produtos(5)
#for produto in produtos[:10]: # Mostrar os 10 primeiros produtos
    #print(produto)
# Implementação do bubble sort

sla = list(map(lambda p: p.preco, produtos))
print("Antes: ", sla)

def quick(arr):
    n = len(arr)
    def quicksort (arr, left, right):
        if left < right: 
            pi = partition(arr, left, right)
            quicksort(arr, left, pi-1)
            quicksort(arr, pi +1, right)
            
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i = i + 1 
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i+1
    
    quicksort(arr, 0, len(arr) - 1)



print("############################################")

quick(sla)

print("Depois: ")
print(sla)