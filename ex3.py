from datetime import date

class Funcionario:
    def __init__(self, identificacao, sobrenome, nome, data_nasc, data_admissao, salario):
        self.identificacao = identificacao
        self.sobrenome = sobrenome
        self.nome = nome
        self.data_nasc = data_nasc
        self.data_admissao = data_admissao
        self.salario = salario

    def idade(self):
        dia_nasc, mes_nasc, ano_nasc = self.data_nasc
        hoje = date.today()
        anos = hoje.year - ano_nasc
        if (hoje.month, hoje.day) < (mes_nasc, dia_nasc):
            anos -= 1
        return anos

    def tempo_de_servico(self):
        dia_adm, mes_adm, ano_adm = self.data_admissao
        hoje = date.today()
        anos = hoje.year - ano_adm
        if (hoje.month, hoje.day) < (mes_adm, dia_adm):
            anos -= 1
        return anos

    def aumento_de_salario(self):
        tempo = self.tempo_de_servico()
        if tempo < 5:
            self.salario *= 1.02
        elif tempo < 10:
            self.salario *= 1.05
        else:
            self.salario *= 1.10

    def mostrarFuncionario(self):
        print(f"Número de identificação: {self.identificacao}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade()}")
        print(f"Tempo de serviço: {self.tempo_de_servico()} ano(s)")
        print(f"Salário atual: {self.salario:.2f}")

if __name__ == "__main__":
    agente = Funcionario("007", "Bond", "James", (11, 11, 1976), (1, 1, 1996), 7500.00)
    agente.aumento_de_salario()
    agente.mostrarFuncionario()
