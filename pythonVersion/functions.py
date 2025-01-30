import os
import time

def verifyExit():
    resposta = input("Deseja 'sair'? ")
    return resposta.lower() == "sair"

def answerToWhatToDo():
    number = int(input(
        '''O que deseja fazer agora? Você tem 3 opções:

        1: Adicionar um usuário
        2: Ver todos os usuários
        3: Ver um usuário específico
        
        Escolha um número: '''
        ))
    
    return number

def getNewUserInformations(usersList):
    name = input("Digite o nome do novo usuário: ")

    age = input("Digite a idade deste usuário: ")

    email = input("Digite o email deste usuário: ")

    usersList.append({'name': name, 'age': age, 'email': email})
    print("Usuário adicionado com sucesso!")

    time.sleep(2)

    os.system('cls')

    return usersList

def seeAllUsers(usersList):
    if len(usersList) > 0:
        for user in usersList:
            time.sleep(0.5)
            print(f"Nome: {user['name']} E-mail: {user['email']} Idade: {user['age']}\n")
            return usersList
    else:
        time.sleep(0.5)

        os.system('cls')

        print('Nenhum usuário cadastrado!')

        return usersList

    


def seeEspecificUser(userList):
    userName = input("Escreva o nome do usuário que deseja visualizar: ")
    found = False
    for user in userList:
        if user['name'].lower() == userName.lower():
            print(f"Usuário encontrado: Nome: {user['name']}, Idade: {user['age']}, Email: {user['email']}")
            found = True
            break

    if not found:
        print("Nome não encontrado na lista.")