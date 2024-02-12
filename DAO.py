from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categorias.txt', 'a') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines('\n')
        

    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arquivo:
            cls.categorias = arquivo.readlines()
        cls.categorias = list(map(lambda x : x.replace('\n', ''), cls.categorias))

        categorias = [Categoria(i) for i in cls.categorias]
        return categorias
   

class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open('vendas.txt', 'a') as arquivo:
            arquivo.writelines(venda.itemVendido.nome + ' | ' 
                               + str(venda.itemVendido.preco) + ' | ' 
                               + venda.itemVendido.categoria + ' | '
                               + venda.vendedor + ' | '
                               + venda.comprador + ' | '
                               + str(venda.quantidadeVendida) + ' | '
                               + venda.data)
            arquivo.writelines('\n')

    
    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arquivo:
            cls.vendas = arquivo.readlines()
        cls.vendas = list(map(lambda x : x.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda x : x.split(' | '), cls.vendas))

        vendas = [Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]) for i in cls.vendas]
        return vendas


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arquivo:
            arquivo.writelines(produto.nome + ' | ' + str(produto.preco) + ' | ' + produto.categoria + ' | ' + str(quantidade))
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arquivo:
            cls.estoque = arquivo.readlines()

        cls.estoque = list(map(lambda x : x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x : x.split(' | '), cls.estoque))
        
        estoque = [Estoque(Produto(i[0], i[1], i[2]), i[3]) for i in cls.estoque if len(cls.estoque) > 0]
        return estoque
    

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor:Fornecedor):
        with open('fornecedores.txt', 'a') as arquivo:
            arquivo.writelines(fornecedor.nome + ' | ' + fornecedor.cnpj + ' | ' + fornecedor.telefone + ' | ' + fornecedor.categoria)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arquivo:
            cls.fornecedores = arquivo.readlines()

        cls.fornecedores = list(map(lambda x : x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x : x.split(' | '), cls.fornecedores))

        fornecedores = [Fornecedor(i[0], i[1], i[2], i[3]) for i in cls.fornecedores]
        return fornecedores
    

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa:Pessoa):
        with open('clientes.txt', 'a') as arquivo:
            arquivo.writelines(pessoa.nome + ' | ' + pessoa.telefone + ' | ' + 
                               pessoa.cpf + ' | ' + pessoa.email + ' | ' + pessoa.endereco)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arquivo:
            cls.clientes = arquivo.readlines()
        
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split(' | '), cls.clientes))

        clientes = [Pessoa(i[0], i[1], i[2], i[3], i[4]) for i in cls.clientes]
        return clientes


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario:Funcionario):
        with open('funcionarios.txt', 'a') as arquivo:
            arquivo.writelines(funcionario.clt + ' | ' + funcionario.nome + ' | ' + funcionario.telefone + ' | ' +
                               funcionario.cpf + ' | ' + funcionario.email + ' | ' + funcionario.endereco)
            arquivo.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arquivo:
            cls.funcionarios = arquivo.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split(' | '), cls.funcionarios))

        funcionarios = [Funcionario(i[0], i[1], i[2], i[3], i[4], i[5] ) for i in cls.funcionarios]
        return funcionarios
    