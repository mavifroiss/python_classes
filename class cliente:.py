class cliente:
    def __init__(self,nome,anoNascimento,sexo,saldo,endereco,ativo):
        self.nome = nome 
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo 
        self.endereco = endereco
        self.ativo = ativo

    def imprimir(self):
        print("nome", self.nome)
        print("ano", self.anoNascimento)
        print("sexo", self.sexo)
        print("saldo", self.saldo)
        print("endereco", self.endereco)
        print("ativo", self.ativo)

    def ValidaClilente(self):  
        if self.ativo:
            print("O cliente", self.nome, "está ativo")   
        else:  
            print("O cliente", self.nome, "não esta ativo.")

            def CalculoIdade(self):
                anoAtual = 2024 
                idadeCliente = 
        
objeto = cliente("Maria", 2006, "F", 760, "Av. Santos Dumont", True)
objeto2 = cliente("Maria", 2006, "F", -760, "Av. Santos Dumont", True)
objeto3 = cliente("Maria", 2006, "F", 760, "Av. Santos Dumont", False)

#objeto.imprimir() 
#objeto2.imprimir()                  
#objeto3.imprimir()

objeto.ValidaClilente()                                                                  
objeto2.ValidaClilente()                                                                  
objeto3.ValidaClilente()     

