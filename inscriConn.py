import json

dataBase = "dataBase.json"
dicty = {}
  

def inscription():
    contenu = {} 
    name = input("Entrez votre nom\n")
    mail = input("Entrez votre E-mail\n")
    password = input("entrez votrez mot de passe\n")
    with open(dataBase) as f:
        try:
            contenu = json.load(f)
        except json.decoder.JSONDecodeError:
            dicty[mail] = {
                "nom" : name,
                "password" : password
            }
        
            exist = True
        else:
            if mail not in contenu:
                dicty[mail] = {
                    "nom" : name,
                    "password" : password
                }

                exist = True
            else:
                print("Ce mail existe deja \nVeuillez vous reconnecter")
                inscriptionConnexion = int(input("Voulez vous  vous inscrit ou vous conntez ? \nTapez 1 pour vous inscrit ou 2 pour vous connetez\n"))

    if exist == True and mail.endswith('@gmail.com'):
        contenu.update(dicty)

        with open(dataBase,"w") as f:
            json.dump(contenu,f,indent=4)
        print(f"incription reussi\nBienvenue M. 2{ dicty[mail]['nom']}")
    else:
        print("votre e-mail n'est pas correct")
    

def loging():

    """[se connecter]

------cette partie permet a l'utilisateur de se connecter------

    """
    
    mail = input("Entrez votre E-mail\n")
    password = input("entrez votrez mot de passe\n")
    with open(dataBase) as f:
        contenu = json.load(f)
        if mail in contenu:
            print(f"Bienvenue M. {contenu[mail]['nom']}")
        else:
            print("")

inscriptionConnexion = int(input("Voulez vous  vous inscrit ou vous conntez ? \nTapez 1 pour vous inscrit ou 2 pour vous connetez\n"))


exist = False

if inscriptionConnexion == 1:
    inscription()
else:
    loging()