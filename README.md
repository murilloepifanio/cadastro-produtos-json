# Cadastro de Produtos com JSON

Projeto desenvolvido em **Python** para praticar o cadastro e gerenciamento de produtos utilizando arquivos **JSON** para armazenamento dos dados.

## Funcionalidades

O sistema foi desenvolvido para permitir:

* Cadastrar produtos
* Listar produtos cadastrados
* Remover produtos
* Armazenar os dados em arquivo JSON
* Recuperar os dados armazenados
* Interagir com o sistema através de um menu

## Menu do sistema

```text
===== CADASTRO DE PRODUTOS =====

1 - Cadastrar produto
2 - Listar produtos
3 - Remover produto
0 - Sair
```

## Estrutura dos dados

Cada produto pode possuir informações como:

```json
{
    "nome": "Notebook",
    "preco": 3500.00,
    "quantidade": 5
}
```

Os produtos são armazenados em um arquivo:

```text
arquivo.json
``
```
