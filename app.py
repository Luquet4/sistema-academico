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

def pegar_nome(lista):
    return [att.nome for att in lista if hasattr(att, "nome") and att.nome]

def continuar(msg):
    while True:
        resp = pedir_input(msg, type=int)
        if resp == 1:
            return True
        elif resp == 2:
            return False
        else:
            print("Opção Inválida!")

def gerar_codigo(lista, prefixo):
    while True:
        codigo = f"{prefixo}{randint(1000, 9999)}"
        if codigo not in [item.codigo for item in lista]:
            return codigo

def gerar_nome(lista, nomes_possiveis):
    while True:
        nome = faker.random_element(nomes_possiveis)
        if nome not in [item.nome for item in lista]:
            return nome

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

    def matricular():
        while True:
            try:
                print("- MATRICULA DE ALUNOS -")
                lista_alunos.append(Pessoas(
                        nome=pedir_input("Nome do Aluno: ", type=str),
                        matricula=f"MAT{randint(1000, 9999)}",
                        data_nasc=pedir_input("Data de Nascimento: ", type=str),
                        sexo=pedir_input("M ou F - ", type=str),
                        endereco=pedir_input("Endereço: ", type=str),
                        telefone=pedir_input("Telefone: ", type=float),
                        email=pedir_input("E-mail: ", type=str)
                    ))
                print(f"Selecione a turma para o aluno {lista_alunos[-1].nome}")
                turma = selecionar_id(lista_turmas)
                lista_turmas[turma].alunos.append(lista_alunos[-1].matricula)
                print(f"\nMatricula N°: {lista_alunos[-1].matricula.upper()} do aluno {lista_alunos[-1].nome.upper()} na turma {lista_turmas[turma].nome.upper()} com as seguintes matriculas {lista_turmas[turma].alunos}\n")
                if not continuar("Deseja realizar outra matricula? 1- Sim, 2- Não\n"):
                    break
            except Exception as e:
                print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Data Nascimento: {self.data_nasc}, Sexo: {self.sexo}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"
    
class Professor(Pessoas):
    def __init__(self, nome, matricula, data_nasc, sexo, endereco, telefone, email, disciplina):
        super().__init__(nome, matricula, data_nasc, sexo, endereco, telefone, email)
        self.disciplina = disciplina if disciplina else None

    def cadastrar_pf():
        while True:
            try:
                print("- CADASTRO PROFESSOR -")
                if not lista_disciplinas:
                    raise ValueError("Não há disciplinas cadastradas para selecionar.")
                    
                lista_professores.append(Professor(
                        nome=pedir_input("Nome do professor: ", type=str),
                        matricula=f"MAT{randint(1000, 9999)}",
                        data_nasc=pedir_input("Data de Nascimento: ", type=str),
                        sexo=pedir_input("M ou F - ", type=str),
                        endereco=pedir_input("Endereço: ", type=str),
                        telefone=pedir_input("Telefone: ", type=float),
                        email=pedir_input("E-mail: ", type=str),
                        disciplina=lista_disciplinas[selecionar_id(lista_disciplinas)].nome
                    ))
                listar(lista_professores)
                if not continuar("Deseja realizar outro cadastro? 1- Sim, 2- Não\n"):
                    break
            except Exception as e:
                print(f"Erro: {e}")

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Disciplina: {self.disciplina}, Data Nascimento: {self.data_nasc}, Sexo: {self.sexo}, Email: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}"

class Disciplinas:
    def __init__(self, nome, codigo, carga_horaria, professor):
        self.nome = nome
        self.codigo = codigo
        self.ch = carga_horaria
        self.professor = professor

    def cadastrar_disciplina():
        while True:
            try:
                print("- CADASTRO DE DISCIPLINAS -\n")
                nome = pedir_input("Nome da Disciplina: ", type=str)
                if nome in [disciplina.nome for disciplina in lista_disciplinas]:
                    print("Essa disciplina já está cadastrada!")
                    continue
                lista_disciplinas.append(Disciplinas(
                    nome=nome, 
                    codigo=f"A{randint(1000,1999)}", 
                    carga_horaria=pedir_input("Carga Horária: ", type=int), 
                    professor=[]
                ))
                listar(lista_disciplinas)
                if not continuar("Cadastro realizado com sucesso! Deseja realizar novamente? 1- Sim, 2- Não\n"):
                    break
            except Exception as e:
                print(e)

    def atribuir_professor():
        while True:
            try:
                print("Selecione a disciplina que deseja atribuir um professor abaixo -\n")
                disc = selecionar_id(lista_disciplinas)
                
                print(f"Escolha o professor para a disciplina selecionada - {lista_disciplinas[disc].nome}\n")
                prof = selecionar_id(lista_professores)

                if not lista_professores[prof].disciplina:

                    lista_disciplinas[disc].professor.append(lista_professores[prof].nome)
                    lista_professores[prof].disciplina = lista_disciplinas[disc].nome
                    print(f"\nO professor {lista_professores[prof].nome} foi atribuido a disciplina {lista_disciplinas[disc].nome}\n")
                    listar(lista_disciplinas)

                    if not continuar("Deseja realizar outra atribuição? 1- Sim, 2- Não\n"):
                        break
                else:
                    print("Professor já atribuido a outra disciplina!")
            except Exception as e:
                 print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Carga Horária: {self.ch}, Professores Responsável: {self.professor}"

class Turmas:
    def __init__(self, nome, codigo, disciplina, professor, alunos):
        self.nome = nome
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = alunos

    def cadastrar_turma():
        while True:
            try:
                print("- CADASTRO DE TURMAS -\n")
                nome = pedir_input("Nome da Turma: ", type=str)
                if nome in [turma.nome for turma in lista_turmas]:
                    print("Essa turma já está cadastrada!")
                    continue
                lista_turmas.append(Turmas(
                    nome=nome, 
                    codigo=f"A{randint(1000,1999)}", 
                    disciplina=None, 
                    professor=None, 
                    alunos=[]
                ))
                listar(lista_turmas)
                if not continuar("Cadastro realizado com sucesso! Deseja realizar novamente? 1- Sim, 2- Não\n"):
                    break
            except Exception as e:
                print(e)

    def atribuir_disciplina_a_turma():
        while True:
            try:
                print("Selecione a turma à qual deseja atribuir uma disciplina")
                turma = selecionar_id(lista_turmas)
                print("Escolha a disciplina a ser atribuída à turma")
                disciplina = selecionar_id(lista_disciplinas)
                lista_turmas[turma].disciplina = lista_disciplinas[disciplina].nome
                print(f"\nA disciplina {lista_disciplinas[disciplina].nome} foi atribuída à turma {lista_turmas[turma].nome}")
                listar(lista_turmas)

                if not continuar("Deseja realizar outra atribuição? 1- Sim, 2- Não\n"):
                    break
            except Exception as e:
                print(e)

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Disciplina: {self.disciplina}, Professor: {self.professor}, Alunos: {self.alunos}"



lista_alunos = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []

lista_alunos = [Pessoas(nome=faker.name(), 
        matricula=gerar_codigo(lista_alunos, "MAT"), 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email()
    ) for _ in range(30)]

lista_professores = [Professor(
        nome=faker.name(), 
        matricula=gerar_codigo(lista_professores, "MAT"), 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email(), 
        disciplina=None
    ) for _ in range(3)]

for _ in range(3):
    nome = gerar_nome(lista_disciplinas, ["Matemática", "Inglês", "Português", "Algoritmos"])
    codigo = gerar_codigo(lista_disciplinas, "A")
    carga_horaria = randrange(20, 120, 10)
    lista_disciplinas.append(Disciplinas(nome=nome, codigo=codigo, carga_horaria=carga_horaria, professor=[]))

for i in range(3):
    nome = gerar_nome(lista_turmas, ["TADS 1", "TADS 2", "TADS 3", "Engenharia da Computação 1"])
    codigo = gerar_codigo(lista_turmas, "A")
    disciplina = lista_disciplinas[i]
    professor = lista_professores[i].nome
    alunos = [lista_alunos[j].matricula for j in range(10)]
    lista_turmas.append(Turmas(nome=nome, codigo=codigo, disciplina=disciplina, professor=professor, alunos=alunos))


def menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n- MENU PRINCIPAL -")
        print("1 - Matricular Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Cadastrar Disciplina")
        print("4 - Cadastrar Turma")
        print("5 - Atribuir Professor a Disciplina")
        print("6 - Atribuir Disciplina a Turma")
        print("7 - Listar Alunos")
        print("8 - Listar Professores")
        print("9 - Listar Disciplinas")
        print("10 - Listar Turmas")
        print("0 - Sair")
        
        opcao = pedir_input("Escolha uma opção: ", type=int)
        
        if opcao == 1:
            Pessoas.matricular()
        elif opcao == 2:
            Professor.cadastrar_pf()
        elif opcao == 3:
            Disciplinas.cadastrar_disciplina()
        elif opcao == 4:
            Turmas.cadastrar_turma()
        elif opcao == 5:
            Disciplinas.atribuir_professor()
        elif opcao == 6:
            Turmas.atribuir_disciplina_a_turma()
        elif opcao == 7:
            listar(lista_alunos)
            input("\nPressione ENTER para continuar...")
        elif opcao == 8:
            listar(lista_professores)
            input("\nPressione ENTER para continuar...")
        elif opcao == 9:
            listar(lista_disciplinas)
            input("\nPressione ENTER para continuar...")
        elif opcao == 10:
            listar(lista_turmas)
            input("\nPressione ENTER para continuar...")
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor, escolha uma opção válida!")

menu()
