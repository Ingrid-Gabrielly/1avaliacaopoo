class Veiculo(App):
    def __init__(self, marca, modelo, ano, categoria, transmissao, combustivel):
        self.marca
        self.modelo
        self.ano
        self.categoria
        self.transmissao
        self.combustivel

    def listarcarro(self):
        if len(self.ListaCarro)>0:
            for i, car in enumerate(self.ListaCarro):
                print(f"Carro {i+1}: ")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Categoria: {car['categoria']}")
                (f"Transmissão: {car['transmissao']}")
                print(f"Combustível: {car['combustivel']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
                print(f"Aluguel:{car['aluguel']}")

            print(f"Total de veículos é: {len(self.ListaCarro)}\n")
        else:
            print("\nOps... Nenhum veículo para listar!")

    def buscarcarro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print(f"Ano: {car['ano']}")
                    print(f"Categoria: {car['categoria']}")
                    print(f"Transmissão: {car['transmissao']}")
                    print(f"Combustível: {car['combustivel']}")
                    print(f"Marca: {car['marca']}")
                    print(f"Modelo: {car['modelo']}")
                    print(f"Aluguel:{car['aluguel']}")
                    break
        else:
            print("Ops... Nenhum veículo cadastrado")

    def buscarcarro_alugar(self):
        if len(self.ListaCarro)>0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car['aluguel'] =="ALUGADO":
                    print("Nenhum veículo disponível para alugar!")
                else:
                    if car['placa']==self.placa:
                        print(f"Placa: {car['placa']}")
                        print(f"Ano: {car['ano']}")
                        print(f"Categoria: {car['categoria']}")
                        print(f"Transmissão: {car['transmissao']}")
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

    def existe_carro(self):
        if len(self.ListaCarro)>0:
            for car in self.ListaCarro:
                if car['placa']==self.placa:
                    return True
        return False

    def categoria(self): 
        while True:
            print("1 - Sedan\n2 - Picape\n3 - SUV\n4 - Hatch")
            while True:
                try:
                    ctg= int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")
            if ctg==1:
                self.categoria= "SEDAN"
                break
            elif ctg==2:
                self.categoria= "PICAPE"
            elif ctg==3:
                self.categoria= "SUV"
                break
            elif ctg==4:
                self.categoria= "HATCH"
            else:
                print("\nInválida")

    def transmissao(self):
        while True:
            print("\n1 - Manual\n2 - Automático")
            while True:
                try:
                    trns=int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")
            if trns==1:
                self.transmissao= "MANUAL"
                break
            elif trns==2:
                self.transmissao= "AUTOMATICO"
                break
            else:
                print("\nInválida")

    def combustivel(self):
        while True:
            print("\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - GNV\n5 - Diesel")
            while True:
                try:
                    cmbst=int(input("\nDigite: "))
                    break
                except ValueError:
                    print("Não aceita letras!\n")
            if cmbst==1:
                self.combustivel= "GASOLINA"
                break
            elif cmbst==2:
                self.combustivel= "ALCOOL"
                break
            elif cmbst==3:
                self.combustivel= "FLEX"
                break
            elif cmbst==4:
                self.combustivel= "GNV"
                break
            elif cmbst==5:
                self.combustivel= "DIESEL"
                break
            else:
                print("\nInválida")

    def novo_carro(self):
        while True:
            self.placa = str(input("\n\nplaca: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema")
                      
        self.ano=int(input("Ano: "))
        Veiculo.categoria(self)
        Veiculo.transmissao(self)
        Veiculo.combustivel(self)

        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        self.aluguel = "DISPONIVEL"
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'aluguel': self.aluguel
        }
        self.ListaCarro.append(carro)
        print(self.ListaCarro)


                   

                
    


class Carro(Veiculo):
    def __init__(self, placa, km, valordiaria):
        self.placa
        self.km
        self.valordiaria



    

