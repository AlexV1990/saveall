#! /usr/bin/env python3

'''
Fonctions de manipulation du fichier de configuration
'''

import json

CONF_FILE_NAME = "conf.json"


'''
check_conf_valid: vérifie que le fichier de conf est bien dans un format json valide
entrée: pas d'argument (nom du fichier dépend de la variable globale CONF_FILE_NAME)
sortie: retourne 0 si le fichier est valide, -1 sinon
'''
def check_conf_valid():
  
  try:
    with open(CONF_FILE_NAME) as data_file:    
      data = json.load(data_file)
    return 0

  except:
    return -1




    
'''
get_list_equipment_from_conf: renvoie la liste des équipements contenus dans le fichier conf.json
entrée: pas d'argument
sortie: liste de tuples (nom de l'equipement, ip de l'equipement) 
''' 
def get_list_equipment_from_conf():

  with open(CONF_FILE_NAME) as data_file:    
    data = json.load(data_file)

  list_eq = []
  
  for dat in data["EQUIPEMENTS"]:
    var_nom = str(data["EQUIPEMENTS"][dat]["NOM"])
    var_ip = str(data["EQUIPEMENTS"][dat]["IP"])
    tuple_eq = (var_nom, var_ip)
    list_eq.append(tuple_eq)

  return list_eq





'''
get_list_equipment_from_conf: renvoie la liste des équipements contenus dans le fichier conf.json
entrée: pas d'argument
sortie: liste de tuples (nom de l'equipement, "", False) 
''' 
def get_list_equipment_from_conf_for_checklist():


  with open(CONF_FILE_NAME) as data_file:    
    data = json.load(data_file)

  list_eq = []
  
  for dat in data["EQUIPEMENTS"]:
    var_nom = str(data["EQUIPEMENTS"][dat]["NOM"])
    tuple_eq = (var_nom, "", False)
    list_eq.append(tuple_eq)

  return list_eq




'''
get_list_files_from_conf: renvoie la liste des fichiers contenus dans le fichier conf.json
entrée: pas d'argument
sortie: liste de tuples (nom de l'equipement, ip de l'equipement) 
''' 
def get_list_files_from_conf():

    with open(CONF_FILE_NAME) as data_file:    
        data = json.load(data_file)

    list_fic = []
    for dat in data["FICHIERS"]:

      var_nom = str(data["FICHIERS"][dat]["NOM"])
      var_path = str(data["FICHIERS"][dat]["PATH"])
      tuple_eq = (var_nom, var_path)
      list_fic.append(tuple_eq)

    return list_fic





'''
delete_file_from_conf: supprime un fichier du fichier de configuration
entrée: nom du fichier à supprimer
sortie: 0 si OK, -1 autrement
'''
def delete_file_from_conf(file_name):

  try:
    with open(CONF_FILE_NAME) as data_file:    
          data = json.load(data_file)

    for element in data["FICHIERS"]:
        if file_name == data["FICHIERS"][element]["NOM"]:
            data["FICHIERS"].pop(element)
            break

    with open(CONF_FILE_NAME, 'w') as data_file:
        data = json.dump(data, data_file)

    return 0
  
  except:
    return -1





'''
delete_equipment_from_conf: supprime un équipement du fichier de configuration
entrée: nom de l'équipement à supprimer
sortie: 0 si OK, -1 autrement
'''
def delete_equipment_from_conf(equipment_name):

  try:
    with open(CONF_FILE_NAME) as data_file:    
          data = json.load(data_file)

    for element in data["EQUIPEMENTS"]:
        if equipment_name == data["EQUIPEMENTS"][element]["NOM"]:
            data["EQUIPEMENTS"].pop(element)
            break

    with open(CONF_FILE_NAME, 'w') as data_file:
        data = json.dump(data, data_file)

    return 0
  
  except:
    return -1





'''
add_file_to_conf: ajoute un fichier de configuration
entrée: liste avec les paramètres du fichier [nom, path, type, equipement]
sortie: 0 si OK, -1 si le nom existe déjà, -2 si autre erreur
'''
def add_file_to_conf(list_params_file):

  file_name = list_params_file[0]
  file_path = list_params_file[1]
  file_type = list_params_file[2]
  equipment_name = list_params_file[3]

  try:
    with open(CONF_FILE_NAME) as data_file:    
          data = json.load(data_file)

    #vérification de l'unicité du nom
    for element in data["FICHIERS"]:
        if file_name == data["FICHIERS"][element]["NOM"]:
            return -1

    #on formate les paramètres du fichier en JSON
    data["FICHIERS"][file_name] = {}
    data["FICHIERS"][file_name]["NOM"] = file_name
    data["FICHIERS"][file_name]["TYPE"] = file_type  
    data["FICHIERS"][file_name]["EQUIPEMENT"] = equipment_name
    data["FICHIERS"][file_name]["PATH"] = file_path

    #On modifie le fichier de configuration
    with open(CONF_FILE_NAME, 'w') as data_file:
        data = json.dump(data, data_file)

    return 0
  
  except:
    return -1