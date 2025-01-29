# Só pra me cituar em como ficaria em python, pra entender a logica

from functions import getNewUserInformations, answerToWhatToDo


usersList = []
print("Bem vindo ao banco de dados de Usuários!!")
answer = answerToWhatToDo()

if answer == 1:
    getNewUserInformations(usersList=usersList)
elif answer == 2:
    pass
else:
    pass