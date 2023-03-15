class App(object):

    def __init__(self):
        self.ListadeClientes = []
        self.ListadeCarros = []
        self.AlugueldeCarro = []
        self.menu()
    
    def alugar(self):
        
        self.cpf = str(input("Digite seu CPF: "))#cadastrar um novo cpf
        while True:
            if not Cliente.cliente_existente(self):#verificar se é um cpf já cadastrado
                print("Novo Cadastro Realizado")
                Cliente.cliente_novo(self)
            else:
                break
            Carro.listar_carro(self)
            Carro.buscar_carros_disponiveis(self)
            App.lista_aluguel(self)

    def lista_aluguel(self):
        alugado = {
            'nome': self.nome,
            'cpf': self.cpf,
            'placa': self.placa,
            'categoria': self.categoria,
            'ano': self.ano,
            'cambio': self.cambio,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel
        }
        self.AlugueldeCarro.append(alugado)
        print("Carro alugado!!")
        print(self.AlugueldeCarro)

    def lista_alugados(self):
            if len(self.AlugueldeCarro) > 0:
                for q, loc in enumerate(self.AlugueldeCarro):
                    print(f"Carro {q+1}:")
                    print(f"Nome: {loc['nome']}")
                    print(f"CPF: {loc['cpf']}")
                    print(f"Placa: {loc['placa']}")
                    print(f"Categoria: {loc['categoria']}")
                    print(f"Ano: {loc['ano']}")
                    print(f"Cambio: {loc['cambio']}")
                    print(f"Combustível: {loc['combustivel']}")
                    print(f"Marca: {loc['marca']}")
                    print(f"Modelo: {loc['modelo']}")
                    print(f"Aluguel:{loc['aluguel']}")
                    print(f"Número de veículos alugados é: {len(self.AluguelCarro)}\n")
                else:
                     print("\nNenhum veículo alugado! ")
    def menu(self):
        while True:
            print("Bem Vindo a locadora DESESPERADOS")
            print("1 - Cadastrar novo veículo")
            print("2 - Cadastrar novo cliente")
            print("3 - Locação de veículo")
            print("4 - Relatório de locação")
            print("5 - Busca de veículos cadastrados")
            print("6 - Busca de clientes cadastrados")
            print("7 - Relatório de veículos cadastrados")
            print("8 - Relatório de clientes cadastrados")
            print("9 - Finalizar o programa!  ")
            while True:
                    try:
                        opc = int(input("\nDigite: "))
                        break
                    except ValueError:
                        print("\nNão aceita letras!\n")
 
                    if opc == 1:
                        Carro.carro_novo(self)
 
                    elif opc == 2:
                         Cliente.cliente_novo(self)
 
                    elif opc == 3:
                         App.alugar(self)
 
                    elif opc == 4:
                        App.lista_aluguel(self)
 
                    elif opc == 5:
                        Carro.buscar_carro(self)
 
                    elif opc == 6:
                        Cliente.buscar_cliente(self)
 
                    elif opc == 7:
                        Carro.listar_carro(self)
 
                    elif opc == 8:
                        Cliente.listar_cliente(self)
 
                    elif opc == 9: 
                        print("\nFinalizado!!!")
                        break
 
                    else:
                         print("\nInválido!\n")

#Classe Veiculo
class Veiculo(App):
    def __init__(self, marca, modelo, ano, categoria, transmissao, combustivel):  #função com os atributos necessários
        self.marca #marca do veículo
        self.modelo #modelo do veículo
        self.ano #ano do veículo
        self.categoria #categorias do veículo
        self.cambio #o veículo é manual ou automático
        self.combustivel #o tipo de combustível do veículo

    def listarcarro(self):
        if len(self.ListadeCarro)>0:
            for i, car in enumerate(self.ListadeCarro):
                print(f"Carro {i+1}: ")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Categoria: {car['categoria']}")
                print(f"Câmbio: {car['cambio']}")
                print(f"Combustível: {car['combustivel']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
                print(f"Aluguel:{car['aluguel']}")

            print(f"Total de veículos é: {len(self.ListadeCarro)}\n")
        else:
            print("\nOps... Nenhum veículo para listar!")

    def buscarcarro(self): #função para buscar carro já cadastrado na locadora
        if len(self.ListadeCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper() #o carro cadastrado será procurado pela placa informada
            for car in self.ListadeCarro:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print(f"Ano: {car['ano']}")
                    print(f"Categoria: {car['categoria']}")
                    print(f"Câmbio: {car['cambio']}")
                    print(f"Combustível: {car['combustivel']}")
                    print(f"Marca: {car['marca']}")
                    print(f"Modelo: {car['modelo']}")
                    print(f"Aluguel:{car['aluguel']}")
                    break
        else:
            print("Ops... Nenhum veículo cadastrado")

    def buscarcarro_alugar(self): #função para ver a disponibilidade de veículos para alugar
        if len(self.ListadeCarro)>0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListadeCarro:
                if car['aluguel'] =="ALUGADO":
                    print("Nenhum veículo disponível para alugar!")
                else:
                    if car['placa']==self.placa:
                        print(f"Placa: {car['placa']}")
                        print(f"Ano: {car['ano']}")
                        print(f"Categoria: {car['categoria']}")
                        print(f"Câmbio: {car['cambio']}")
                        print(f"Combustível: {car['combustivel']}")
                        print(f"Marca: {car['marca']}")
                        print(f"Modelo: {car['modelo']}")
                        print(f"Aluguel:{car['aluguel']}")

                        if car['aluguel']=="ALUGADO":
                            print("O veículo já está locado!")
                        else:
                            car['aluguel']="ALUGADO"
        else:
            print("Nenhum veículo disponível para alugar!")

    def existecarro(self): #função para saber se existe algum carro cadastrado na locadora com a placa informada 
        if len(self.ListadeCarro)>0:
            for car in self.ListadeCarro:
                if car['placa']==self.placa:
                    return True
        return False

    def categoria(self): #função para escolher qual categoria de carro deseja
        while True:
            print("1 - Sedan\n2 - Picape\n3 - SUV\n4 - Hatch")
            while True:
                try:
                    catego= int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")
            if catego==1:
                self.categoria= "SEDAN"
                break
            elif catego==2:
                self.categoria= "PICAPE"
            elif catego==3:
                self.categoria= "SUV"
                break
            elif catego==4:
                self.categoria= "HATCH"
            else:
                print("\nInválida")

    def cambio(self): #função para escolher se é um carro automático ou manual
        while True:
            print("\n1 - Manual\n2 - Automático")
            while True:
                try:
                    transmissao=int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")
            if transmissao==1:
                self.cambio= "MANUAL"
                break
            elif transmissao==2:
                self.cambio= "AUTOMATICO"
                break
            else:
                print("\nInválida")

    def combustivel(self): #função para escolher qual o tipo de combustível 
        while True:
            print("\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - GNV\n5 - Diesel")
            while True:
                try:
                    combust=int(input("\nDigite: "))
                    break
                except ValueError:
                    print("Não aceita letras!\n")
            if combust==1:
                self.combustivel= "GASOLINA"
                break
            elif combust==2:
                self.combustivel= "ALCOOL"
                break
            elif combust==3:
                self.combustivel= "FLEX"
                break
            elif combust==4:
                self.combustivel= "GNV"
                break
            elif combust==5:
                self.combustivel= "DIESEL"
                break
            else:
                print("\nInválida")

    def novocarro(self): #função para cadastrar novo carro
        while True: 
            self.placa = str(input("\n\nplaca: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema") #se a placa digitada estiver no sistema, apresentará essa frase
                      
        self.ano=int(input("Ano: "))
        Veiculo.categoria(self)
        Veiculo.cambio(self)
        Veiculo.combustivel(self)

        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        self.aluguel = "DISPONIVEL"
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'cambio': self.cambio,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel
        }
        self.ListadeCarro.append(carro)
        print(self.ListadeCarro)

#Classe Carro
class Carro(Veiculo):
    def __init__(self, placa, km, valordiaria):
        self.placa
        self.km
        self.valordiaria

#CLASSE CLIENTE
class Cliente(App):
 
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
 
    def listar_cliente(self):
        if len(self.ListadeCliente) > 0:
            for i, clt in enumerate(self.ListadeCliente):
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"ID: {clt['id']}")
            print(f"O total de clientes é: {len(self.ListadeCliente)}\n")
        else:
            print("\nNão há cliente para listar!\n")
 
    def buscar_cliente(self):
        if len(self.ListadeCliente) > 0:
            self.cpf = str(input("Digite o ID: ")).upper()
            for car in self.ListadeCliente:
                if car['id'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"ID: {car['id']}")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")
 
    def existe_cliente(self):
        if len(self.ListadeCliente) > 0:
            for clt in self.ListadeCliente:
                if clt['id'] == self.id:
                    return True
        return False
 
    def cliente_novo(self):
        while True:
            self.id = str(input("Digite a ID: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print(" Usuário já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        usuario = {
            'nome': self.nome,
            'id': self.id
        }
 
        self.ListadeCliente.append(usuario)
        print(self.ListadeCliente)

    

