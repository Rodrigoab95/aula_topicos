import os
os.system('cls')

nomeProduto = input("Informe o nome do produto: ")
valorProduto = float(input("Informe o valor do produto: "))


desc = 0.00
if valorProduto < 0:
    print("Informe um valor válido!")
elif valorProduto >= 50 and valorProduto < 200:
    desc = 0.05
elif valorProduto >= 200 and valorProduto < 500:
    desc = 0.06
elif valorProduto >= 500 and valorProduto < 1000:
    desc = 0.07
elif valorProduto >= 1000:
    desc = 0.08

produtoDesc = valorProduto * desc

print("{} \n{} \n{}".format(nomeProduto,round(valorProduto,1),(valorProduto - produtoDesc)))