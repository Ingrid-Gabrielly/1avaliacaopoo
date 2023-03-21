import datetime
class App(object):
    def __init__(self):
        self.ListaCliente = []
        self.ListaCarro = []
        self.AluguelCarro = []
        self.menu()

    def alugar(self):
 
        ide = str(input("Digite o ID (seu CPF): "))
        while True:
            if not Cliente.existe_cliente(self, ide):
                print("Novo Cadastro!")
                clienteselecionado = Cliente.novo_cliente(self)
            else:
                clienteselecionado=Cliente.cliente_existente(self, ide)
                break    
        Carro.listar_carro(self)
        carroselecionado= Carro.buscar_carro_alugar(self)
        dias = int(input("Quantos dias deseja alugar? "))
        carroselecionado.alugardias(dias)
        clienteselecionado.adicionarnohistorico(carroselecionado)

    def lista_alugados(self):
        if len(self.AluguelCarro) > 0:
            for carros in self.AluguelCarro:
                print(carros) 
        else:
            print("\nNenhum veículo alugado para listar!")
 
    def devolver(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car.placa == self.placa:
                    carroselecionado=car
                    dias = int(input("Quantos dias alugou? "))
                    carroselecionado.devolvercarro(dias)
                    break
                else:
                    print("Nenhum veiculo cadastrado!\n")   

    def mostrar_historico(self):
        ide = str(input("Digite o ID (seu CPF): "))
        while True:
            if not Cliente.existe_cliente(self, ide):
                print("Cliente não existe")
            else:
                clienteselecionado=Cliente.cliente_existente(self, ide)
                break
        clienteselecionado.consultarhistorico()
        
    def menu(self):
        while True:
            print("Bem Vindo a locadora DESESPERADOS")
            print("1- Cadastrar novo veículo")
            print("2- Cadastrar novo cliente")
            print("3- Locação de veículo")
            print("4- Devolver veículo")
            print("5- Busca de veículos cadastrados")
            print("6- Busca de clientes cadastrados")
            print("7- Relatório de veículos cadastrados")
            print("8- Relatório de clientes cadastrados")
            print("9- Histórico de clientes")
            print("0- Finalizar o programa!")
           
            opc = int(input("\nDigite o número da operação que deseja realizar: "))
                       
            if opc == 1:
                Carro.novo_carro(self)
 
            elif opc == 2:
                Cliente.novo_cliente(self)
 
            elif opc == 3:
                App.alugar(self)
 
            elif opc == 4:
                App.devolver(self)
 
            elif opc == 5:
                Carro.buscar_carro(self)
 
            elif opc == 6:
                Cliente.buscar_cliente(self)
 
            elif opc == 7:
                Carro.listar_carro(self)
 
            elif opc == 8:
                Cliente.listar_cliente(self)

            elif opc == 9:
                App.mostrar_historico(self)

            elif opc == 0: 
                print("\nFinalizado!")
                break
 
            else:
                print("\nInválido!\n")
                break

class Veiculo(App):
    def __init__(self, marca, modelo, ano, aluguel):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.aluguel = aluguel
        self.alugado = False

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, aluguel, placa, km, valordiaria):
        super().__init__(marca, modelo, ano, aluguel)
        self.placa = placa
        self.km = km
        self.valordiaria = int(valordiaria)
    
    
    def alugardias(self, tempo):
        self.tempo=int(tempo)
        self.alugado = True

        self.aluguelapagar=self.tempo*self.valordiaria
        print(f"Valor a ser pago é: R${self.aluguelapagar}")


    def devolvercarro(self, dias):
        self.diasdevolvel = int(dias)
        self.atrasado = False
        self.alugado = False

        if (self.diasdevolvel>self.tempo):
            self.atrasado = True
            self.diasatrasados = self.diasdevolvel-self.tempo

        if (self.atrasado==True):
            self.valortotal=(self.valordiaria * self.tempo) + ((self.valordiaria+(self.valordiaria*0.20))*self.diasatrasados)

            print(f"Valor a ser pago é: {self.valortotal}")

        else:
            if self.tempo>self.diasdevolvel:
                self.valortotal=self.valordiaria*self.diasdevolvel
                print(f"Valor a ser pago é: {self.valortotal}")
            else:
                self.valortotal=self.valordiaria*self.tempo
                print(f"Valor a ser pago é: {self.valortotal}")

        self.aluguelapagar=self.valortotal        

    def listar_carro(self):
        if len(self.ListaCarro) > 0:
            for carro in self.ListaCarro:
                print (carro)     
        else:
            print("\nNenhum veículo para listar! ")

    def buscar_carro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car.placa == self.placa:
                    print(car)
                    break
                else:
                    print("Nenhum veiculo cadastrado!\n")

    def buscar_carro_alugar(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car.alugado == False:
                    print("Nenhum veiculo disponível para alugar!")
                    if car.placa == self.placa:
                        print(car)
                        if car.alugado == True:
                            print("O veículo já está locado!")
                        else:
                            car.alugado = True    
                            return car                         
        else:
            print("Nenhum veiculo disponível para alugar!")

    def existe_carro(self):
        if len(self.ListaCarro) > 0:
            for car in self.ListaCarro:
                if car.placa == self.placa:
                    return True
        return False
    
    def novo_carro(self):
 
        while True:
            self.placa = str(input("\n\nDigite a placa: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema")
        self.ano = int(input("Ano: "))
        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        self.km = str(input("Digite a quilometragem: ")).upper()
        self.valordiaria = str(input("Valor da diária: R$")).upper()
        self.aluguel = "DISPONIVEL"
        carro = Carro(self.marca, self.modelo, self.ano, self.aluguel, self.placa, self.km, self.valordiaria)
        self.ListaCarro.append(carro)


    def __str__(self):
        if(self.alugado == True):
            aluguel = "ALUGADO"
        else:
            aluguel = "DISPONIVEL PARA ALUGAR"

        return f"marca: {self.marca}\nmodelo: {self.modelo}\nano: {self.ano}\nplaca: {self.placa}\nkm: {self.km}\nvalordiaria: {self.valordiaria}\n {aluguel}"

#Classe cliente
class Cliente(App):
 
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.historico=[]

    def consultarhistorico(self):
        if len(self.historico)>0:
            for carros in self.historico:
                print(carros)

    def adicionarnohistorico(self, carro):
        self.historico.append(carro)

    def listar_cliente(self):
        if len(self.ListaCliente) > 0:
            for cliente in self.ListaCliente:
                print(cliente)
        else:
            print("\nNenhum cliente para listar!\n")
 
    def buscar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o ID (seu CPF): ")).upper()
            for car in self.ListaCliente:
                if car.id == self.cpf:
                    print(car)                    
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")
 
    def existe_cliente(self, cpf):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt.id == cpf:
                    return True
        return False
    
    def cliente_existente(self, cpf):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt.id == cpf:
                    return clt
    
    def novo_cliente(self):
        while True:
            ide = str(input("Digite o ID (seu CPF): "))
            if not Cliente.existe_cliente(self, ide):
                break
            else:
                print("Já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        usuario = Cliente(self.nome, ide)
 
        self.ListaCliente.append(usuario)
        return usuario

    def __str__(self):
        return f"id: {self.id}\nnome: {self.nome}\n"
    
App()