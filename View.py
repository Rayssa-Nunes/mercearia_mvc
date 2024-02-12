import Controllers
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')


criarArquivos('categorias.txt', 'clientes.txt', 'estoque.txt', 'fornecedores.txt', 'funcionarios.txt', 'vendas.txt')

if __name__ == '__main__':

    while True:
        local = int(input(
            'Digite 1 para acessar ( Categorias )\n'
            'Digite 2 para acessar ( Estoque )\n'
            'Digite 3 para acessar ( Fornecedores )\n'
            'Digite 4 para acessar ( Clientes )\n'
            'Digite 5 para acessar ( Funcionários )\n'
            'Digite 6 para acessar ( Vendas )\n'
            'Digite 7 para ver os produtos mais vendidos\n'
            'Digite 8 para sair\n'
        ))

        if local == 1:
            cat = Controllers.ControllerCategoria()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma categoria\n'
                                    'Digite 2 para remover uma categoria\n'
                                    'Digite 3 para alterar uma categoria\n'
                                    'Digite 4 para mostrar as categorias cadastradas\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar: ')
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover: ')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar: ')
                    novaCategoria = input('Digite a categoria para qual deseja alterar: ')
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                elif decidir == 5:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue

        elif local == 2:
            cat = Controllers.ControllerEstoque()
            while True:
                decidir = int(input('Digite 1 para cadastrar um produto\n'
                                    'Digite 2 para remover um produto\n'
                                    'Digite 3 para alterar um produto\n'
                                    'Digite 4 para ver o estoque\n'
                                    'Digite 5 para sair\n'))
                
                if decidir == 1:
                    nome = input('Digite o nome do produto: ')
                    preco = input('Digite o valor do produto: ')
                    categoria = input('Digite a categoria do produto: ')
                    quantidade = input('Digite a quandidade do produto: ')
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produtoRemover = input('Digite o nome do produto que deseja remover: ')
                    cat.removerProduto(produtoRemover)
                elif decidir == 3:
                    produtoAlterar = input('Digite o nome do produto que deseja alterar: ')
                    novoNome = input('Digite o novo nome do produto: ')
                    novoPreco = input('Digite o novo preço do produto: ')
                    novaCategoria = input('Digite a nova categoria do produto: ')
                    novaQuantidade = input('Digite a nova quantidade do produto: ')
                    cat.alterarProduto(produtoAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                elif decidir == 5:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue
        elif local == 3:
            cat = Controllers.ControllerFornecedor()
            while True:
                decidir = int(input('Digite 1 para cadastrar um fornecedor\n'
                                    'Digite 2 para remover um fornecedor\n'
                                    'Digite 3 para alterar um fornecedor\n'
                                    'Digite 4 para mostrar os fornecedores cadastrados\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    nome = input('Digite o nome do fornecedor: ')
                    cnpj = input('Digite o cnpj do fornecedor: ')
                    telefone = input('Digite o telefone do fornecedor: ')
                    categoria = input('Digite a categoria do fornecedor: ')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    fornecedor = input('Digite a nome do fornecedor que deseja remover: ')
                    cat.removerFornecedor(fornecedor)
                elif decidir == 3:
                    nome = input('Digite o nome do fornecedor: ')
                    novoNome = input('Digite o novo nome do fornecedor: ')
                    novoCnpj = input('Digite o novo cnpj do fornecedor: ')
                    novoTelefone = input('Digite o novo telefone do fornecedor: ')
                    novaCategoria = input('Digite a nova categoria do fornecedor: ')
                    cat.alterarFornecedor(nome, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarFornecedor()
                elif decidir == 5:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue
        
        elif local == 4:
            cat = Controllers.ControllerCliente()
            while True:
                decidir = int(input('Digite 1 para cadastrar um cliente\n'
                                    'Digite 2 para remover um cliente\n'
                                    'Digite 3 para alterar um cliente\n'
                                    'Digite 4 para mostrar os clientes cadastrados\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    nome = input('Digite o nome do cliente: ')
                    telefone = input('Digite o telefone do cliente: ')
                    cpf = input('Digite o cpf do cliente: ')
                    email = input('Digite o E-mail do cliente: ')
                    endereco = input('Digite o endereço do cliente: ')
                    cat.cadastrarCliente(nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    cliente = input('Digite a nome do cliente que deseja remover: ')
                    cat.removerCliente(cliente)
                elif decidir == 3:
                    nome = input('Digite o nome do cliente: ')
                    novoNome = input('Digite o novo nome do cliente: ')
                    novoTelefone = input('Digite o novo telefone do cliente: ')
                    novoCpf = input('Digite o novo cpf do cliente: ')
                    novoEmail = input('Digite o novo E-mail do cliente: ')
                    novoEndereco = input('Digite o novo endereço do cliente: ')
                    cat.alterarCliente(nome, novoNome, novoTelefone, novoCpf, novoEmail, novoTelefone)
                elif decidir == 4:
                    cat.mostrarClientes()
                elif decidir == 5:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue
        
        elif local == 5:
            cat = Controllers.ControllerFuncionario()
            while True:
                decidir = int(input('Digite 1 para cadastrar um funcionário\n'
                                    'Digite 2 para remover um funcionário\n'
                                    'Digite 3 para alterar um funcionário\n'
                                    'Digite 4 para mostrar os funcionários cadastrados\n'
                                    'Digite 5 para sair\n'))
                if decidir == 1:
                    clt = input('Digite a clt do funcionário: ')
                    nome = input('Digite o nome do funcionário: ')
                    telefone = input('Digite o telefone do funcionário: ')
                    cpf = input('Digite o cpf do funcionário: ')
                    email = input('Digite o E-mail do funcionário: ')
                    endereco = input('Digite o endereço do funcionário: ')
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    funcionario = input('Digite a nome do funcionário que deseja remover: ')
                    cat.removerFuncionario(funcionario)
                elif decidir == 3:
                    novaClt = input('Digite a nova clt do funcionário: ')
                    nome = input('Digite o nome do funcionário: ')
                    novoNome = input('Digite o novo nome do funcionário: ')
                    novoTelefone = input('Digite o novo telefone do funcionário: ')
                    novoCpf = input('Digite o novo cpf do funcionário: ')
                    novoEmail = input('Digite o novo E-mail do funcionário: ')
                    novoEndereco = input('Digite o novo endereço do funcionário: ')
                    cat.alterarFuncionario(novaClt, nome, novoNome, novoTelefone, novoCpf, novoEmail, novoTelefone)
                elif decidir == 4:
                    cat.mostrarFuncionario()
                elif decidir == 5:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue

        elif local == 6:
            cat = Controllers.ControllerVenda()
            while True:
                decidir = int(input('Digite 1 para cadastrar uma venda\n'
                                    'Digite 2 para mostrar as vendas cadastrados\n'
                                    'Digite 3 para sair\n'))
                if decidir == 1:
                    nomeProduto = input('Digite o nome do produto: ')
                    vendedor = input('Digite o nome vendedor: ')
                    comprador = input('Digite o nome do comprador: ')
                    quantidadeVendida = input('Digite a quantidade vendida: ')
                    cat.cadastrarVenda(nomeProduto, vendedor, comprador, quantidadeVendida)
                elif decidir == 2:
                    dataInicio = input('Digite a data de início no formato dia/mês/ano: ')
                    dataTermino = input('Digite a data de término no formato dia/mês/ano: ')
                    cat.mostrarVenda(dataInicio, dataTermino)
                elif decidir == 3:
                    break
                else:
                    print('\033[31mDigite um número válido!\033[m')
                    continue

        elif local == 7:
            cat = Controllers.ControllerVenda()
            cat.relatorioProdutos()

        elif local == 8: 
            break
        else:
            print('\033[31mDigite um número válido!\033[m')

                    


        