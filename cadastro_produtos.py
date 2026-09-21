produtos=[]
def cadastrar_produto(**dados):
    produtos.append(dados)
    with open('arquivo.json','w') as arquivo:
        json.dump(dados,arquivo,ensure_ascii=False,indent=4)
def listar_produtos():
    with open('arquivo.json','r') as arquivo:
       produtos_cadastrados=json.load(arquivo)
       print(produtos_cadastrados)
def menu():
    print('''

    ===== CADASTRO DE PRODUTOS =====

1 - Cadastrar produto
2 - Listar produtos
3 - Remover produto
0 - Sair

    ''')
if __name__=='__main__':
    menu()
