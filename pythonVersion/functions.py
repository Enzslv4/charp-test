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

    if any(user['name'] == name for user in usersList):
        print("Usuário já existe no sistema.")
    elif any(user['age'] == age for user in usersList):
        print("Usuário já existe no sistema.")
    elif any(user['email'] == email for user in usersList):
        print("Usuário já existe no sistema.")
    else:
        usersList.append({'name': name, 'age': age, 'email': email})
        print("Usuário adicionado com sucesso!")
        return usersList

def showAllUsers(usersList):
    i = 0
    for user in usersList:
        print(f"Usuário {i}: 
            Nome: {user[i]['name']}, Idade: {user[i]['age']}, E-mail: {user[i]['email']}")
        i += 1

# lists = []
# getNewUserInformations(lists)
# getNewUserInformations(lists)
# print(lists)

i = 0
print(f'{i + 1}')