# -*- coding:utf-8 -*-
# //////////////////////////////////////////////////////////////////////////////////////////////////
#                       Chiffrement par base
# //////////////////////////////////////////////////////////////////////////////////////////////////




def encryption(basePath, message):

    # Open the base and read contents
    base = open(basePath, "r")
    baseText = base.read()

    # Create a list with base contents
    baseList = []
    for caractere in baseText :
        baseList.append(caractere)
    base.close()


    # Cleaning of initial message
    message = message.lower()
    message = message.replace('é', 'e')
    message = message.replace('è', 'e')
    message = message.replace('ç', 'c')
    message = message.replace('à', 'a')

    # Encryption
    encryptedMessage = []
    for letter in message :
        if letter == " " :
            encryptedMessage.append(" ")
        else :
            compteur = 0
            while letter != baseList[compteur]:
                compteur += 1
            encryptedMessage.append(compteur)
            baseList[compteur] = " "
    
    # Formating the return according to the spaces and by adding "-" between the numbers
    finalMessage = ""
    for i in range(0, len(encryptedMessage)) :
        if i == 0 :
            finalMessage += str(encryptedMessage[i])
        else :
            if encryptedMessage[i] == " " :
                finalMessage += " "
            else :
                if encryptedMessage[i-1] != " ":
                    finalMessage += "-" + str(encryptedMessage[i])
                else :
                    finalMessage += str(encryptedMessage[i])
    return finalMessage




"""
# Try

basePath = r'/home/winston10/Documents/Python/Base_Encoding/Base'

message = "This is a message to cipher"

print(encryption(basePath, message))
"""