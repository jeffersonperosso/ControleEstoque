import os
def cadastraproduto():
        os.system('cls') or None
        nome = input("Nome do produto:")
        qtde = int(input("Quantidade no estoque:"))
        valorcusto = float(input("Valor de custo:"))
        valorvenda = float(input("Valor de venda:"))
        arq = open("produtos.txt","a")
        frase =nome + ";" + str(qtde) + ";" + str(valorcusto) + ";" + str(valorvenda) + ";\n"
        arq.write(frase)
        arq.close()
        input("Produto "+nome+" salvo com sucesso!\n\nPressione qualquer tecla para continuar...")
def acharproduto(nome):
        if os.path.exists("produtos.txt"):
                arq = open("produtos.txt","r")
                produtos = arq.readlines()
                count = 0
                for pro in produtos:
                        pro = pro.split(';')
                        if pro[0] == nome:
                                arq.close()
                                return count
                        count+=1
                arq.close()
        return -1

def alterarproduto():
        os.system('cls') or None
        nome = input("Digite o nome do produto:")
        linha = acharproduto(nome)

        if linha == -1:
                os.system('cls') or None
                input("Produto " + nome + " não foi encontrado!\n\nPressione qualquer tecla para continuar...")
        else:
                arq = open("produtos.txt", "r")
                produtos = arq.readlines()
                arq.close()
                pro = produtos[linha].split(';')
                os.system('cls') or None
                print("[A]Nome: ",pro[0],"\n[C]Valor de custo: ",pro[2],"\n[C]Valor de venda:",pro[3])
                op =input("\n\nQual campo deseja editar?: ")
                os.system('cls') or None
                op = op.upper()
                if op == 'A':
                        pro[0] = input("Novo nome: ")
                if op == 'B':
                        pro[2] = input("Novo valor de custo: ")
                if op == 'C':
                        pro[3] = input("Novo valor de venda: ")
                frase = pro[0] + ";" + pro[1] + ";" + pro[2] + ";" + pro[3] + ";\n"
                produtos[linha] = frase
                arq = open("produtos.txt", "w")
                arq.writelines(produtos)
                arq.close()
                os.system('cls') or None
                input("Produto alterado com sucesso!\n\nPressione qualquer tecla para continuar...")
def excluirproduto():
        os.system('cls') or None
        nome = input("Digite o nome do produto que deseja excluir:")
        linha = acharproduto(nome)
        if linha == -1:
                os.system('cls') or None
                input("Produto " + nome + " não foi encontrado!\n\nPressione qualquer tecla para continuar...")
        else:
                arq = open("produtos.txt", "r")
                produtos = arq.readlines()
                arq.close()
                produtos.pop(linha)
                arq = open("produtos.txt", "w")
                arq.writelines(produtos)
                arq.close()
                os.system('cls') or None
                input("Produto excluido com sucesso!\n\nPressione qualquer tecla para continuar...")
def consultarprodutos():
        os.system('cls') or None
        if os.path.exists("produtos.txt"):
                nome = input("Qual produto deseja consultar?(Caso queira ver todos, somente pressione Enter):")
                if nome == "":
                        arq = open("produtos.txt", "r")
                        produtos = arq.readlines()
                        arq.close()
                        valorcusto = 0
                        valorvenda = 0
                        for pro in produtos:
                                pro = pro.split(';')
                                valorcusto += float(pro[2]) * int(pro[1])
                                valorvenda += float(pro[3]) * int(pro[1])
                                print("Nome: ",pro[0]," Estoque: ",pro[1]," Custo: ",pro[2]," Venda: ",pro[3])
                        print("\nValor total de custo: ",valorcusto," Valor total de venda: ",valorvenda)
                        input("\n\nPressione qualquer tecla para continuar...")
                else:
                        linha = acharproduto(nome)
                        if linha == -1:
                                input("Produto " + nome + " não foi encontrado!\n\nPressione qualquer tecla para continuar...")
                        else:
                                arq = open("produtos.txt", "r")
                                produtos = arq.readlines()
                                arq.close()
                                pro = produtos[linha].split(';')
                                os.system('cls') or None
                                print("Nome: ", pro[0], "\nQuantidade no estoque: ", pro[1],"\nValor de custo: ", pro[2], "\nValor de venda:", pro[3])
                                input("\n\nPressione qualquer tecla para continuar...")
        else:
                input("Nenhum produto foi encontrado!\n\nPressione qualquer tecla para continuar...")
def registrar():
        os.system('cls') or None
        nome = input("Digite o nome do produto:")
        linha = acharproduto(nome)

        if linha == -1:
                os.system('cls') or None
                input("Produto " + nome + " não foi encontrado!\n\nPressione qualquer tecla para continuar...")
        else:
                arq = open("produtos.txt", "r")
                produtos = arq.readlines()
                arq.close()
                pro = produtos[linha].split(';')
                os.system('cls') or None
                print("Nome: ", pro[0], "   Estoque: ", pro[1])
                op = input("\n\nEntrada ou saida(E/S): ")
                op = op.upper()
                if op == 'E':
                        pro[1] = int(pro[1]) + int(input("Entrada: "))
                if op == 'S':
                        pro[1] = int(pro[1]) - int(input("Saida: "))

                frase = pro[0] + ";" + str(pro[1]) + ";" + pro[2] + ";" + pro[3] + ";\n"
                produtos[linha] = frase
                arq = open("produtos.txt", "w")
                arq.writelines(produtos)
                arq.close()
                input("Estoque alterado com sucesso!\n\nPressione qualquer tecla para continuar...")

def menu():
        while True:
                os.system('cls') or None
                print("[A]Cadastrar produto\n[B]Alterar produto\n[C]Excluir produto\n[D]Registrar entrada/saida\n[E]Consultar produtos\n[X]Sair\n\n")

                op = input("Digite a opcao:")
                op = op.upper()
                if op == 'A':
                        cadastraproduto()
                if op == 'B':
                        alterarproduto()
                if op == 'C':
                        excluirproduto()
                if op == 'D':
                        registrar()
                if op == 'E':
                        consultarprodutos()
                if op == 'X':
                    break


menu()


