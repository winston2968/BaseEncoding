# -*- coding:utf-8 -*-
# //////////////////////////////////////////////////////////////////////////////////////////////////
#                       Déchiffrement par base
# //////////////////////////////////////////////////////////////////////////////////////////////////

def decipherment(basePath, message):

    # Open the base and read contents
    base = open(basePath, "r")
    baseText = base.read()

    # Create a list with base contents
    baseList = []
    for caractere in baseText :
        baseList.append(caractere)
    base.close()

    # Formating the message for decipherment
    messageList = message.split(" ")

    # Decipherment
    initialMessage = ""
    for word in messageList :
        wordList = word.split("-")
        for value in wordList :
            initialMessage += baseList[int(value)]
        initialMessage += " "
    return initialMessage
        




"""
basePath = r'/home/winston10/Documents/Python/Base_Encoding/Base'

messageToDecipher = '7-108-2-11 25-30 37 1-5-41-47-51-210-8 13-20 32-52-49-117-17-26'

print(decipherment(basePath, messageToDecipher))
"""