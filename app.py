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
                        data_nasc=pedir_input("Data de Nascimento: ", type=int),
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
                        data_nasc=pedir_input("Data de Nascimento: ", type=int),
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

    def atribuir_disciplina():
        while True:
            try:
                print("Selecione o professor que deseja atribuir uma disciplina abaixo - \n")
                prof = selecionar_id(lista_professores)

                print(f"Escolha a disciplina para atribuir ao professor - {lista_professores[prof].nome}")
                disc = selecionar_id(lista_disciplinas)

                lista_professores[prof].disciplina = lista_disciplinas[disc].nome
                lista_disciplinas[disc].professor.append(lista_professores[prof].nome)

                if not continuar("Deseja atribuir outra disciplina? 1- Sim, 2- Não\n"):
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

    def cadastrar_disciplina():
        while True:
            try:
                print("- CADASTRO DE DISCIPLINAS -\n")
                print("Seleciona o professor da Disciplina -\n")
                indice_professor = selecionar_id(lista_professores)
                
                if not lista_professores[indice_professor].disciplina:
                    lista_disciplinas.append(Disciplinas(
                        nome=pedir_input("Nome da Disciplina: ", type=str), 
                        codigo=f"A{randint(1000,1999)}", 
                        carga_horaria=pedir_input("Carga Horária: ", type=int), 
                        professor=[lista_professores[indice_professor].nome]
                    ))
                    lista_professores[indice_professor].disciplina = lista_disciplinas[-1].nome
                    listar(lista_disciplinas)

                    if not continuar("Cadastro realizado com sucesso! Deseja realizar novamente? 1- Sim, 2- Não\n"):
                        break
                else:
                    print("Professor já associado a outra disciplina.")
                    input("Pressione Enter para continuar...")
                    continue
            except Exception as e:
                print(e)


    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Carga Horária: {self.ch}, Professores Responsável: {self.professor}"
    
class Turmas():
    def __init__(self, nome, codigo, disciplina, professor, alunos):
        self.nome = nome
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = alunos

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

    def listar_disciplinas_por_turma(turma_nome):
        for turma in lista_turmas:
            if turma.nome == turma_nome:
                print(f"Disciplina da turma {turma.nome}: {turma.disciplina}")

    def __str__(self):
        return f"Nome: {self.nome}, Código: {self.codigo}, Disciplina: {self.disciplina}, Professor: {self.professor}, Alunos: {self.alunos}"

lista_alunos = [Pessoas(nome=faker.name(), 
        matricula=f"MAT{randint(1000, 9999)}", 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email()
    ) for _ in range(30)]

lista_professores = [Professor(
        nome=faker.name(), 
        matricula=f"MAT{randint(1000, 9999)}", 
        data_nasc=faker.date_of_birth(), 
        sexo=faker.random_element(["M", "F"]), 
        endereco=faker.address(), 
        telefone=faker.phone_number(), 
        email=faker.email(), 
        disciplina=None
    ) for _ in range(3)]

lista_disciplinas = [Disciplinas(
        nome=faker.random_element(["Matemática", "Inglês", "Português", "Algoritmos"]),
        codigo=f"A{randint(1000, 1999)}",
        carga_horaria=randrange(20, 120, 10),
        professor=[]
    ) for _ in range(3)]

lista_turmas = [Turmas(
        nome=faker.random_element(["TADS 1", "TADS 2", "TADS 3", "Engenharia da Computação 1"]),
        codigo=f"A{randint(1000, 1999)}",
        disciplina=lista_disciplinas[i],
        professor=lista_professores[i].nome,
        alunos=[lista_alunos[j].matricula for j in range(10)]
        ) for i in range(3)]



def menu():
    while True:
        print("\n- MENU PRINCIPAL -")
        print("1 - Matricular Aluno")
        print("2 - Cadastrar Professor")
        print("3 - Cadastrar Disciplina")
        print("4 - Atribuir Professor à Disciplina")
        print("5 - Atribuir Disciplina à Turma")
        print("6 - Listar Alunos")
        print("7 - Listar Professores")
        print("8 - Listar Disciplinas")
        print("9 - Listar Turmas")
        print("0 - Sair")
        
        opcao = pedir_input("Escolha uma opção: ", type=int)
        
        if opcao == 1:
            Pessoas.matricular()
        elif opcao == 2:
            Professor.cadastrar_pf()
        elif opcao == 3:
            Disciplinas.cadastrar_disciplina()
        elif opcao == 4:
            Professor.atribuir_disciplina()
        elif opcao == 5:
            Turmas.atribuir_disciplina_a_turma()
        elif opcao == 6:
            listar(lista_alunos)
        elif opcao == 7:
            listar(lista_professores)
        elif opcao == 8:
            listar(lista_disciplinas)
        elif opcao == 9:
            listar(lista_turmas)
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor, escolha uma opção válida!")

# Chama o menu
menu()
