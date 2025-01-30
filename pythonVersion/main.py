# Só pra me cituar em como ficaria em python, pra entender a logica

from functions import getNewUserInformations, answerToWhatToDo, seeAllUsers, verifyExit, seeEspecificUser
import os


usersList = []
sureToContinue = True
print("Bem vindo ao banco de dados de Usuários!!\n")


while sureToContinue:
    answer = answerToWhatToDo()

    if answer == 1:
        getNewUserInformations(usersList=usersList)
        if verifyExit():
            break
        else:
            os.system('cls')
    elif answer == 2:
        seeAllUsers(usersList=usersList)
        if verifyExit():
            break
        else:
            os.system('cls')
    elif answer == 3:
        seeEspecificUser(userList=usersList)
        if verifyExit():
            break
        else:
            os.system('cls')
    else:
        break
