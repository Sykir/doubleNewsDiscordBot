import dal

def setup():
    getSecret("TOKENBOT")
    getSecret("URLCHECK")
    getSecret("CHANNELID")

def promptSecret(key):
    value = input("Le secret {} n'existe pas. Entrez une valeur pour la créer : ".format(key))
    return value

def getSecret(key):
    value = dal.getSecret(key)
    # check if exist
    if value:
        return value[0][0]
    else:
       setSecret(key)

def setSecret(key):
    value = promptSecret(key)
    dal.setSecret(key, value)