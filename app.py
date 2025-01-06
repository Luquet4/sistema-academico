from faker import Faker
from random import randint, randrange
import os

faker = Faker()

def pedir_input(texto, type):
    while True:
        try:
            valor = type(input(texto))
            return valor
        except ValueError as e:
            print(f"ERRO! {e} Digite o valor correto!")


def listar(lista):
    print("Lista:")
    for i, pessoa in enumerate(lista):
        print(f"ID - {i} - {pessoa}")

def selecionar_id(lista):
    while True:
        try:
            listar(lista)
            resp = pedir_input("Digite o ID desejado: ", type=int)
            return resp
        except Exception as e:
            print(e)

def pegar_cod(lista):
    id = []
    for mat in lista:
        if hasattr(mat, "matricula"):
            id.append(mat.matricula)
        elif hasattr(mat, "codigo"):
            id.append(mat.codigo)
    return id

class Pessoas:
    def __init__(self, nome, matricula, data_nasc, sexo, endereco, telefone, email):
        validar_sexo = lambda x: x.upper() if x.upper() in ["M", "F"] else 'N/A'
        self.nome = nome
        self.matricula = matricula
        self.data_nasc = data_nasc
        self.sexo = validar_sexo(sexo)
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def matricular(lista_alunos):
        while True:
            try:
                if pedir_input("\n1- Preencher com dados ficticios, ou qualquer número para cadastrar manualmente\n", type=int) == 1:
                    lista_alunos.extend([Pessoas(
                        nome=faker.name(),
                        matricula=f"MAT{randint(1000, 9999)}",
                        data_nasc=faker.date_of_birth(),
                        sexo=faker.random_element(["M", "F"]),
                        endereco=faker.address(),
                        telefone=faker.phone_number(),
                        email=faker.email())
                        ])
                else:
                    lista_alunos.append(Pessoas(
                        nome=pedir_input("Nome do Aluno: ", type=str),
                        matricula=f"MAT{randint(1000, 9999)}",
                        data_nasc=pedir_input("Data de Nascimento: ", type=int),
                        sexo=pedir_input("M ou F - ", type=str),
                        endereco=pedir_input("Endereço: ", type=str),
                        telefone=pedir_input("Telefone: ", type=float),
                        email=pedir_input("E-mail: ", type=str)
                    ))
                listar(lista_alunos)
                if pedir_input("\nDeseja realizar outro cadastro? 1- Sim, 2- Não\n", type=int) == 1:
                    os.system("cls")
                    continue
                else:
                    break
            except Exception as e:
                print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Data Nascimento: {self.data_nasc}, Sexo: {self.sexo}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"
    
class professor(Pessoas):
    def __init__(self, nome, matricula, data_nasc, sexo, endereco, telefone, email, disciplina):
        super().__init__(nome, matricula, data_nasc, sexo, endereco, telefone, email)
        self.disciplina = disciplina

    def cadastrar_pf():
        while True:
            try:
                if pedir_input("\n1- Preencher com dados ficticios, 2+- Cadastrar Manualmente\n", type=int) == 1:
                    lista_professores.extend([professor(
                        nome=faker.name(), 
                        matricula=f"MAT{randint(1000, 9999)}", 
                        data_nasc=faker.date_of_birth(), 
                        sexo=faker.random_element(["M", "F"]), 
                        endereco=faker.address(), 
                        telefone=faker.phone_number(), 
                        email=faker.email(), 
                        disciplina=faker.random_element(pegar_cod(lista_disciplinas)))])
                    pegar_cod(lista_disciplinas)
                else:
                    lista_professores.append(professor(
                        nome=pedir_input("Nome do professor: ", type=str),
                        matricula=f"MAT{randint(1000, 9999)}",
                        data_nasc=pedir_input("Data de Nascimento: ", type=int),
                        sexo=pedir_input("M ou F - ", type=str),
                        endereco=pedir_input("Endereço: ", type=str),
                        telefone=pedir_input("Telefone: ", type=float),
                        email=pedir_input("E-mail: ", type=str),
                        disciplina=pedir_input("Disciplina: ", type=str)
                    ))
                listar(lista_professores)
                if pedir_input("\nDeseja realizar outro cadastro? 1- Sim, 2- Não\n", type=int) == 1:
                    os.system("cls")
                    continue
                else:
                    break
            except Exception as e:
                print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Disciplina: {self.disciplina}, Data Nascimento: {self.data_nasc}, Sexo: {self.sexo}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

class Disciplinas:
    def __init__(self, nome, codigo, carga_horaria, professor):
        self.nome = nome
        self.codigo = codigo
        self.ch = carga_horaria
        self.professor = professor
    
    def atribuir_professor():
        while True:
            try:
                print("Selecione a disciplina que deseja atribuir um professor abaixo -\n")
                disc = selecionar_id(lista_disciplinas)
                print(f"Escolha o professor para a disciplina selecionada - {lista_disciplinas[disc].nome}\n")
                prof = selecionar_id(lista_professores)

                lista_disciplinas[disc].professor.append(lista_professores[prof].nome)
                lista_professores[prof].disciplina = lista_disciplinas[disc].nome
                print(f"O professor {lista_professores[prof].nome} foi atribuido a disciplina {lista_disciplinas[disc].nome}")
                if pedir_input("Deseja realizar outra atribuição? 1- Sim, 2- Não\n", type=int) == 1:
                    os.system("cls")
                    continue
                else:
                    break
            except Exception as e:
                 print(e)

    def cadastrar_disciplina():
        while True:
            try:
                print("- CADASTRO DE DISCIPLINAS -\n")
                lista_disciplinas.append(Disciplinas(
                    nome=pedir_input("Nome da Disciplina: ", type=str), 
                    codigo=f"A{randint(1000,1999)}", 
                    carga_horaria=pedir_input("Carga Horária: ", type=int), 
                    professor=[lista_professores[selecionar_id(lista_professores)].nome]))
                
                if lista_disciplinas[-1].professor != []:
                    lista_professores
                listar(lista_disciplinas)
            except Exception as e:
                print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Carga Horária: {self.ch}, Professores Responsável: {self.professor}"

lista_disciplinas = [Disciplinas(
        nome=faker.random_element(["Matemática", "Inglês", "Português", "Algoritmos"]),
        codigo=f"A{randint(1000, 1999)}",
        carga_horaria=randrange(20, 120, 10),
        professor=[]
    ) for _ in range(3)]

lista_alunos = [Pessoas(nome=faker.name(), 
        matricula=f"MAT{randint(1000, 9999)}", 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email()
    ) for _ in range(3)]

lista_professores = [professor(
        nome=faker.name(), 
        matricula=f"MAT{randint(1000, 9999)}", 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email(), 
        disciplina=None
    ) for _ in range(3)]


professor.cadastrar_pf()