from Models import *
from DAO import *

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria: 
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('\033[32mCategoria cadastrada com sucesso\033[m')
        else:
            print('A categoria que deseja cadastrar já existe')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        categoria = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(categoria) == 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('categorias.txt', 'w') as arquivo:
                for i in x:
                    arquivo.writelines(i.categoria)
                    arquivo.writelines('\n')
        
        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade) 
                           if (x.produto.categoria) == categoriaRemover else (x), estoque))
        
        with open('estoque.txt', 'w') as arquivo:
            for i in estoque:
                arquivo.writelines(i.produto.nome + ' | ' + str(i.produto.preco) + ' | ' + i.produto.categoria + ' | ' + str(i.quantidade))
                arquivo.writelines('\n') 
        
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        categoria = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(categoria) > 0:
            categoria1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(categoria1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else (x), x))
                print('\033[32mCategoria alterada com sucesso\033[m')

                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) 
                                if (x.produto.categoria) == categoriaAlterar else (x), estoque))
                
                with open('estoque.txt', 'w') as arquivo:
                    for i in estoque:
                        arquivo.writelines(i.produto.nome + ' | ' + str(i.produto.preco) + ' | ' + i.produto.categoria + ' | ' + str(i.quantidade))
                        arquivo.writelines('\n') 
                
            else:
                print('A categoria que deseja alterar já existe')
        
        else:
            print('A categoria que deseja alterar não existe')

        with open('categorias.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.categoria)
                arquivo.writelines('\n')


    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')
            

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        h = list(filter(lambda x: x.categoria == categoria, y))
        estoque = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(estoque) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('\033[32mProduto cadastrado com sucesso\033[m')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')
    
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        estoque = list(filter(lambda x: x.produto.nome == nome, x))
        if len(estoque) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('\033[32mProduto removido com sucesso\033[m')
            with open('estoque.txt', 'w') as arquivo:
                for i in x:
                    arquivo.writelines(i.produto.nome + ' | ' + str(i.produto.preco) + ' | ' + i.produto.categoria + ' | ' + str(i.quantidade))
                    arquivo.writelines('\n')
        else:
            print('O produto que deseja remover não existe')


    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            estoque = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(estoque) > 0:
                estado = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(estado) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nomeAlterar) else (x), x))
                    print('\033[32mProduto alterado com sucesso\033[m')
                else:
                    print('Produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe')
            
            with open('estoque.txt', 'w') as arquivo:
                for i in x:
                    arquivo.writelines(i.produto.nome + ' | ' + str(i.produto.preco) + ' | ' + i.produto.categoria + ' | ' + str(i.quantidade))
                    arquivo.writelines('\n')

        else:
            print('A categoria informada não existe')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print('=' * 10,'Produtos', '=' * 10)
            for i in estoque:
                
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}')
                print('-' * 30)


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if not existe:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * float(i.produto.preco)

                        DaoVenda.salvar(vendido)
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arquivo = open('estoque.txt', 'w')
        arquivo.write('')
        
        for i in temp:
            arquivo.writelines(i[0].nome + ' | ' + str(i[0].preco) + ' | ' + i[0].categoria + ' | ' + str(i[1]))
            arquivo.writelines('\n')
        arquivo.close()

        if not existe:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não contém no estoque')
            return None
        else:
            print('\033[32mVenda realizada com sucesso\033[m')
            return valorCompra
        
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itemVendido.nome
            quantidade = int(i.quantidadeVendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + quantidade} 
                                    if (x['produto'] == nome) else (x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'{"=" * 5} Produto [{a}] {"=" * 5}')
            print(f'Produto: {i["produto"]}\n'
                    f'Quantidade: {i["quantidade"]}\n')
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                  and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f'{"=" * 10} Venda [{cont}] {"=" * 10})\n')
            print(f'Nome: {i.itemVendido.nome}\n'
                  f'Categoria: {i.itemVendido.categoria}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: {i.comprador}\n'
                  f'Vendedor: {i.vendedor}')
            total += float(i.itemVendido.preco) * int(i.quantidadeVendida)
            cont += 1

        print(f'Total vendido: {total}')


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(listaCnpj) > 0:
            print('\033[33mO cnpj já existe\033[m')
        elif len(listaTelefone) > 0:
            print('\033[33mO telefone já existe\033[m')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('\033[31mDigite um cnpj ou telefone válido\033[m')
        
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria) if (x.nome == nomeAlterar) else (x), x))
            else:
                print('\033[33mCnpj já existe\033[m')
        else:
            print('\033[33mO fornecedor que deseja alterar não existe\033[m')

        with open('fornecedores.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.nome + ' | ' + i.cnpj + ' | ' + i.telefone + ' | ' + str(i.categoria))
                arquivo.writelines('\n')
            print('\033[32mFornecedor alterado com sucesso\033[m')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('\033[33mO fornecedor que deseja remover não existe\033[m')
            return None
        
        with open('fornecedores.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.nome + ' | ' + i.cnpj + ' | ' + i.telefone + ' | ' + str(i.categoria))
                arquivo.writelines('\n')
            print('\033[32mFornecedor removido com sucesso\033[m')


    def mostrarFornecedor(self):
        x = DaoFornecedor.ler()
        if len(x) == 0:
            print('\033[33mLista de fornecedores vazia\033[m')

        for i in x:
            print(f'{"=" * 10} Fornecedor {"=" * 10}')
            print(f'Nome: {i.nome}\n'
                  f'Cnpj: {i.cnpj}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Categoria: {i.categoria}\n')


class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('\033[33mCPF já existente\033[m')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('\033[32mCliente cadastrado com sucesso!\033[m')
            else:
                print('\033[31mDigite um cpf ou telefone válido\033[m')


    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else (x), x))
        else:
            print('\033[33mO cliente que deseja alterar não existe\033[m')

        with open('clientes.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.nome + ' | ' + i.telefone + ' | ' + i.cpf + ' | ' + i.email + ' | ' + i.endereco)
                arquivo.writelines('\n')
            print('\033[32mCliente alterado com sucesso\033[m')

        
    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if i.nome == nome:
                    del x[i]
                    break
        else:
            print('\033[33mO cliente que deseja remover não existe\033[m')
            return None
        
        with open('clientes.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.nome + ' | ' + i.telefone + ' | ' + i.cpf + ' | ' + i.email + ' | ' + i.endereco)
                arquivo.writelines('\n')
            print('\033[32mCliente removido com sucesso\033[m')


    def mostrarClientes(self):
        x = DaoPessoa.ler()
        if len(x) == 0:
            print('\033[33mLista de clientes vazia\033[m')

        for i in x:
            print(f'{"=" * 10} Cliente {"=" * 10}')
            print(f'Nome: {i.nome}\n'
                  f'Cpf: {i.telefone}\n'
                  f'E-mail: {i.email}\n'
                  f'Endereço: {i.endereco}\n'
                  f'CPF: {i.cpf}\n'
                  f'CLT: {i.clt}\n')


class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listaClt = list(filter(lambda x: x.clt == clt, x))
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('\033[33mO cpf já existe\033[m')
        elif len(listaClt) > 0:
            print('\033[33mJá existe um funcionário com essa clt\033[m')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
            else:
                print('\033[31mDigite um cpf ou telefone válido\033[m')
        
    def alterarFuncionario(self, novaClt, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cpf == novoCpf, x))
            if len(est) == 0:
                x = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else (x), x))
            else:
                print('\033[33mCpf já existe\033[m')
        else:
            print('\033[33mO funcionário que deseja alterar não existe\033[m')

        with open('funcionarios.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.clt, i.nome + ' | ' + i.telefone + ' | ' + i.cpf + ' | ' + i.email + ' | ' + i.endereco)
                arquivo.writelines('\n')
            print('\033[32mFuncionário alterado com sucesso\033[m')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('\033[33mO funcionário que deseja remover não existe\033[m')
            return None
        
        with open('funcionarios.txt', 'w') as arquivo:
            for i in x:
                arquivo.writelines(i.clt + ' | ' + i.nome + ' | ' + ' | ' + i.telefone + ' | ' + i.cpf + ' | ' + i.email +  ' | ' + i.endereco)
                arquivo.writelines('\n')
            print('\033[32mFuncionário removido com sucesso\033[m')


    def mostrarFuncionario(self):
        x = DaoFuncionario.ler()
        if len(x) == 0:
            print('\033[33mLista de funcionários vazia\033[m')

        for i in x:
            print(f'{"=" * 10} Funcionário {"=" * 10}')
            print(f'Nome: {i.nome}\n'
                  f'Telefone: {i.telefone}\n'
                  f'E-mail: {i.email}\n'
                  f'Endereço: {i.endereco}\n'
                  f'CPF: {i.cpf}\n'
                  f'CLT: {i.clt}\n')
