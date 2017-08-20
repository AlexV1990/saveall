#! /usr/bin/env python3
# coding: utf-8

'''
Fonctions de manipulation et vérifications du fichier de configuration
'''

import json
import utils.misc as misc

CONF_FILE_NAME = "conf/conf.json"


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
add_file_to_conf: ajoute un fichier dans le fichier de configuration
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





'''
add_equipment_to_conf: ajoute un équipement dans le fichier de configuration
entrée: liste avec les paramètres de l'équipement [nom, IP, type, login, MDP]
sortie: 0 si OK, -1 si le nom existe déjà, -2 si autre erreur
'''
def add_equipment_to_conf(list_params_equipment):

  equipment_name = list_params_equipment[0]
  equipment_ip = list_params_equipment[1]
  equipment_type = list_params_equipment[2]
  equipment_login = list_params_equipment[3]
  equipment_mdp = list_params_equipment[4]

  try:
    with open(CONF_FILE_NAME) as data_file:    
          data = json.load(data_file)

    #vérification de l'unicité du nom
    for element in data["EQUIPEMENTS"]:
        if equipment_name == data["EQUIPEMENTS"][element]["NOM"]:
            return -1

    #on formate les paramètres du fichier en JSON
    data["EQUIPEMENTS"][equipment_name] = {}
    data["EQUIPEMENTS"][equipment_name]["NOM"] = equipment_name
    data["EQUIPEMENTS"][equipment_name]["IP"] = equipment_ip
    data["EQUIPEMENTS"][equipment_name]["TYPE"] = equipment_type  
    data["EQUIPEMENTS"][equipment_name]["LOGIN"] = equipment_login
    data["EQUIPEMENTS"][equipment_name]["MDP"] = equipment_mdp

    #On modifie le fichier de configuration
    with open(CONF_FILE_NAME, 'w') as data_file:
        data = json.dump(data, data_file)

    return 0

  except:
    return -1





'''
check_list_equipment_valid: vérifie que la demande de création d'ajout d'un équipement est valide
entrée: liste de paramètres concernant l'équipement [nom, IP, type, login, MDP]
sortie: retourne 0 si l'équipement peut être ajouté
                 -1 si le nom de l'équipement n'est pas unique
                 -2 si l'IP fournie n'est pas valable
                 -3 si l'IP n'est pas unique
                 -4 si le type n'est pas "DB" (base de données), "S" (serveur), "R" (équipement réseau)
                 -5 si tous les champs ne sont pas remplis

'''
def check_list_equipment_valid(list_params_equipment):

  equipment_name = list_params_equipment[0]
  equipment_ip = list_params_equipment[1]
  equipment_type = list_params_equipment[2]
  equipment_login = list_params_equipment[3]
  equipment_mdp = list_params_equipment[4]

  #Vérification que tous les champs sont remplis
  if equipment_name == "" or equipment_ip == "" or equipment_type == "" or equipment_login == "" or equipment_mdp == "":
    return -5

  #Ouverture du fichier de conf
  with open(CONF_FILE_NAME) as data_file:    
        data = json.load(data_file)

  #Vérification de l'unicité du nom
  if equipment_name in data["EQUIPEMENTS"]:
    return -1

  #Vérification de la validité de l'IP
  if misc.is_valid_ipv4_address(equipment_ip) == False:
    return -2

  #Vérification de l'unicité de l'IP dans le fichier de conf
  for element in data["EQUIPEMENTS"]:
    if equipment_ip in data["EQUIPEMENTS"][element]["IP"]:
      return -3

  #Vérification du type d'équipement
  if equipment_type != "DB" and equipment_type != "S" and equipment_type != "R":
    return -4

  return 0 
