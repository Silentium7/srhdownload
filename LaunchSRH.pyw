#

from os import system, listdir, getcwd, mkdir, startfile, startfile



try : import sys
except ModuleNotFoundError :
    system("pip install sys")
import sys

try : import importlib
except ModuleNotFoundError :
    system("pip install importlib")
import importlib

try : import urllib.request
except ModuleNotFoundError :
    system("pip install urllib3")
import urllib.request

# trouve ou crée le chemin du dossier de SRH
path = "c:/Users/Public"
dossier_SRH_existant = "SRH" in listdir(path)
if not dossier_SRH_existant : mkdir(str(path+"/SRH"))
dossier_SRH_existant = True

# regarde si le fichier SRH existe ou non
path_file = "c:/Users/Public/SRH"
path_SRH = path_file+"/SRH.pyw"
fichier_SRH_existant = "SRH.pyw" in listdir(path_file)
if not fichier_SRH_existant : 
    # essaye de télécharger le fichier SRH
    try : 
        data_file_SRH = urllib.request.urlopen("https://raw.githubusercontent.com/Silentium7/SRH/main/SRH.pyw")
        content = data_file_SRH.readlines()
        with open(path_SRH, 'a') as fic : pass
        with open(path_SRH, 'wb') as fic :
            fic.writelines(content)
    
    except urllib.error.URLError :
        input("Pas de connexion internet...\nSRH n'est pas installé sur votre ordinateur\nRéessayez avec de la connexion")
fichier_SRH_existant = True



# essaye de télecharger la nouvelle version du launcher si il y a de la co
try :
    data_file = urllib.request.urlopen("https://raw.githubusercontent.com/Silentium7/SRH/main/SRH.pyw")
    data = data_file.readlines()
    
    # dernière version
    dernière_version_en_ligne = int(data[0][1:-1])
    
    with open(path_SRH, 'r') as fic :    
        dernière_version_pc = int(fic.readlines()[0][1:-1])

    # si on est à jour, on lance le launcher
    if dernière_version_en_ligne <= dernière_version_pc :
        print("Pas de mise à jour ...\nLancement")
        print(path_SRH)
        startfile(path_SRH)
        
        sys.path.append("C:\\Users\\Public\\SRH")
        from SRH import srhf
        srhf()
    # sinon on fait une update
    else :
        data_file_SRH = urllib.request.urlopen("https://raw.githubusercontent.com/Silentium7/SRH/main/SRH.pyw")
        content = data_file_SRH.readlines()
        with open(path_SRH, 'a') as fic : pass
        with open(path_SRH, 'wb') as fic :
            fic.writelines(content)
        
        # exécute le fichier
        print("Mise à jour faite ...\nLancement")
        
        sys.path.append("C:\\Users\\Public\\SRH")
        from SRH import srhf
        srhf()



# si pas de co alors lance le launcher
except urllib.error.URLError :
    print("Pas de connexion ...\nLancement du Launcher")
    